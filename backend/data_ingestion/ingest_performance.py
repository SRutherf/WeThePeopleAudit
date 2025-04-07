import requests
import json
import datacommons as dc
import datacommons_pandas as dcpd
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://datausa.io/api/data"

def fetch_data_from_api(state):
    # params = {
    #     "drilldowns": "Nation",
    #     "measures": "Population"
    # }
    # response = requests.get(BASE_URL, params=params)
    # response.raise_for_status()  # Raises an error for bad status codes
    # return response.json()
    
    # get data, you need to specify the granularity to get smaller details
    #state, metropolitanArea, county, town/city, zipcodetabulationarea, censustract
    #mass = geoId/25
    ma_counties = dc.get_places_in(['geoId/25'], 'County')
    suffolk_towns = dc.get_places_in(['geoId/25025'], 'City')
    boston_zips = dc.get_places_in(['geoId/2507000'], 'CensusZipCodeTabulationArea')
    zip_tracts = dc.get_places_in(['zip/02130'], 'CensusTract')
    my_tract = dc.get_places_in(['geoId/25025120201'], 'CensusBlockGroup')
    my_block = 'geoId/250251202012'
    print(dc.get_property_labels([my_block]))
    print(dc.get_property_values([my_block], 'name'))
    print(dc.get_property_values([my_block], 'typeOf'))
    print(dc.get_stat_series(my_block, 'Median_Income_Household'))


if __name__ == "__main__":
    # states = dc.get_places_in(['country/USA'], 'State') # returns geoIds in alpha order, geoId/01-50
    
    state = "geoId/25" # Massachusetts
    data = fetch_data_from_api(state)
    # Pretty-print the JSON response
    # print(json.dumps(data, indent=2))