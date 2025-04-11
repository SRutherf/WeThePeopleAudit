import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor
import datacommons as dc
import datacommons_pandas as dcpd
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://datausa.io/api/data"

# use if getting data is too slow
def parallel_get_places(dcids, place_type):
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(lambda dcid: (dcid, dc.get_places_in([dcid], place_type).get(dcid, [])), dcids)
        return dict(results)

# use if network is spotty and you dont want to waste progress
def save_checkpoint(data, step):
    with open(f"data_checkpoint_{step}.json", "w") as f:
        json.dump(data, f, indent=2)

def add_counties(data):
    print("Adding counties")
    states = list(data['states'].keys())
    result = dc.get_places_in(states, 'County')
    for state in states:
        counties = result.get(state, [])
        data['states'][state]['counties'] = {county: {} for county in counties}
    return data

def add_cities(data):
    print("Adding cities")
    counties = [
        county
        for state_data in data['states'].values()
        for county in state_data['counties']
    ]
    result = dc.get_places_in(counties, 'City')
    for state_data in data['states'].values():
        for county in state_data['counties']:
            cities = result.get(county, [])
            state_data['counties'][county]['cities'] = {city: {} for city in cities}
    return data

def add_zipcodes(data):
    print("Adding zipcodes")
    cities = [
        city
        for state_data in data['states'].values()
        for county_data in state_data['counties'].values()
        for city in county_data.get('cities', {})
    ]
    result = dc.get_places_in(cities, 'CensusZipCodeTabulationArea')
    for state_data in data['states'].values():
        for county_data in state_data['counties'].values():
            for city in county_data.get('cities', {}):
                zips = result.get(city, [])
                county_data['cities'][city]['zipcodes'] = {zip_code: {} for zip_code in zips}
    return data

def add_tracts(data):
    print("Adding tracts")
    zips = [
        zip_code
        for state_data in data['states'].values()
        for county_data in state_data['counties'].values()
        for city_data in county_data['cities'].values()
        for zip_code in city_data.get('zipcodes', {})
    ]
    result = dc.get_places_in(zips, 'CensusTract')
    for state_data in data['states'].values():
        for county_data in state_data['counties'].values():
            for city_data in county_data['cities'].values():
                for zip_code in city_data.get('zipcodes', {}):
                    tracts = result.get(zip_code, [])
                    city_data['zipcodes'][zip_code]['tracts'] = {tract: {} for tract in tracts}
    return data

def add_blocks(data):
    print("Adding blocks")
    tracts = [
        tract
        for state_data in data['states'].values()
        for county_data in state_data['counties'].values()
        for city_data in county_data['cities'].values()
        for zip_data in city_data['zipcodes'].values()
        for tract in zip_data.get('tracts', {})
    ]
    result = dc.get_places_in(tracts, 'CensusBlockGroup')
    for state_data in data['states'].values():
        for county_data in state_data['counties'].values():
            for city_data in county_data['cities'].values():
                for zip_data in city_data['zipcodes'].values():
                    for tract in zip_data.get('tracts', {}):
                        blocks = result.get(tract, [])
                        zip_data['tracts'][tract]['blocks'] = {block: block for block in blocks}
    return data

def fetch_state_data(states):
    data = {'states': {state: {} for state in states}}
    data = add_counties(data)
    data = add_cities(data)
    data = add_zipcodes(data)
    data = add_tracts(data)
    data = add_blocks(data)

    return data

def fetch_stat_vars(dcids, stat_vars):
    raw_data = dc.get_stat_all(dcids, stat_vars)

    def extract_statvars_with_best_source(raw_data, stat_vars):
        result = {}

        for dcid, stats in raw_data.items():
            dcid_result = {}

            for stat_var in stat_vars:
                details = stats.get(stat_var)
                if not details:
                    continue

                source_series = details.get("sourceSeries", [])
                best_source = max(source_series, key=lambda s: len(s.get("val", {})), default=None)

                if best_source:
                    dcid_result[stat_var] = {
                        "data": best_source["val"],
                        "source": best_source.get("provenanceDomain", "unkonw"),
                        "unit": best_source.get("unit", "unknown")
                    }

            if dcid_result:
                result[dcid] = dcid_result

        return result

    return extract_statvars_with_best_source(raw_data, stat_vars)

def enrich_with_labels_and_types(data):
    print("fetching geo data")
    dcids = []
    for state_id, state_data in data['states'].items():
        dcids.append(state_id)
        for county_id, county_data in state_data['counties'].items():
            dcids.append(county_id)
            for city_id, city_data in county_data['cities'].items():
                dcids.append(city_id)
                for zip_id, zip_data in city_data['zipcodes'].items():
                    dcids.append(zip_id)
                    for tract_id, tract_data in zip_data['tracts'].items():
                        dcids.append(tract_id)
                        for block_id in tract_data['blocks']:
                            dcids.append(block_id)

    names = dc.get_property_values(dcids, 'name')
    types = dc.get_property_values(dcids, 'typeOf')
    longitudes = dc.get_property_values(dcids, 'longitude')
    latitudes = dc.get_property_values(dcids, 'latitude')

    def set_metadata(obj, dcid):
        if dcid in names and names[dcid]:
            obj['name'] = names[dcid][0]
        if dcid in types and types[dcid]:
            obj['typeOf'] = types[dcid]
        if dcid in longitudes and longitudes[dcid]:
            obj['longitude'] = longitudes[dcid][0]
        if dcid in latitudes and latitudes[dcid]:
            obj['latitude'] = latitudes[dcid][0]

    for state_id, state_data in data['states'].items():
        set_metadata(state_data, state_id)
        for county_id, county_data in state_data['counties'].items():
            set_metadata(county_data, county_id)
            for city_id, city_data in county_data['cities'].items():
                set_metadata(city_data, city_id)
                for zip_id, zip_data in city_data['zipcodes'].items():
                    set_metadata(zip_data, zip_id)
                    for tract_id, tract_data in zip_data['tracts'].items():
                        set_metadata(tract_data, tract_id)
                        for block_id in tract_data['blocks']:
                            tract_data['blocks'][block_id] = {
                                'dcid': block_id
                            }
                            set_metadata(tract_data['blocks'][block_id], block_id)

    #Fetch stat_vars
    print("Fetching performance data")
    stat_vars = [
        'Median_Income_Household', 'UnemploymentRate_Person',
        'Percent_Person_Obesity', 'Percent_Person_Smoking'
    ]
    performance_data = fetch_stat_vars(dcids, stat_vars)

    return data, performance_data

def save_state_geo_data_to_file(geo_data, states):
    abbrs = dc.get_property_values(states, 'fips52AlphaCode')

    for state_id in states:
        state_abbr = abbrs.get(state_id)[0]

        script_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(script_dir, "..", "..", "data", "performance", "states_raw")
        
        filename = f"{state_abbr.lower()}_geo_data.json"
        full_path = os.path.join(save_path, filename)

        state_data = {state_id: geo_data['states'][state_id]}

        with open(full_path, "w") as f:
            json.dump(state_data, f, indent=2)
        
        print(f"Saved state data to {full_path}")

def save_state_perf_data_to_file(performance_data, states):
    abbrs = dc.get_property_values(states, 'fips52AlphaCode')

    for state_id in states:
        state_abbr = abbrs.get(state_id)[0]

        script_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(script_dir, "..", "..", "data", "performance", "states_raw")
        
        filename = f"{state_abbr.lower()}_perf_data.json"
        full_path = os.path.join(save_path, filename)

        with open(full_path, "w") as f:
            json.dump(performance_data, f, indent=2)
        
        print(f"Saved state data to {full_path}")

if __name__ == "__main__":
    # states = dc.get_places_in(['country/USA'], 'State')['country/USA']
    states = ['geoId/25'] # Massachusetts
    data = fetch_state_data(states)
    geo_data, performance_data = enrich_with_labels_and_types(data)
    save_state_geo_data_to_file(geo_data, states)
    save_state_perf_data_to_file(performance_data, states)