import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, "..", "..", "data", "performance", "states_raw")
output_dir = os.path.join(script_dir, "..", "..", "data", "performance", "states_transformed")

os.makedirs(output_dir, exist_ok=True)

def process_geo_file(state_code, input_path):
    geo_data = {
        "states": [],
        "counties": [],
        "cities": [],
        "zips": [],
        "tracts": [],
        "blocks": []
    }

    def process_level(dcid, obj, level, next_level_key):
        if level == "blocks":
            geo_data["blocks"].append({
                "dcid": dcid,
                "name": obj.get("name"),
                "typeOf": obj.get("typeOf", [])
            })
            return
    
        children = list(obj.get(next_level_key, {}).keys()) if next_level_key else []
        record = {
            "dcid": dcid,
            "name": obj.get("name"),
            "typeOf": obj.get("typeOf", []),
            "longitude": obj.get("longitude"),
            "latitude": obj.get("latitude"),
            "children": children
        }
        geo_data[level].append(record)

        # Recurse to next level
        for child_dcid, child_obj in obj.get(next_level_key, {}).items() if next_level_key else []:
            if level == "states":
                process_level(child_dcid, child_obj, "counties", "cities")
            elif level == "counties":
                process_level(child_dcid, child_obj, "cities", "zipcodes")
            elif level == "cities":
                process_level(child_dcid, child_obj, "zips", "tracts")
            elif level == "zips":
                process_level(child_dcid, child_obj, "tracts", "blocks")
            elif level == "tracts":
                process_level(child_dcid, child_obj, "blocks", None)

    # Load the input JSON
    with open(input_path, "r") as f:
        raw = json.load(f)

    # Start recursion from top-level states
    for state_dcid, state_obj in raw.items():
        process_level(state_dcid, state_obj, "states", "counties")

    # Write each geo level to a separate file
    for level, records in geo_data.items():
        out_path = os.path.join(output_dir, f"{state_code}_{level}.json")
        with open(out_path, "w") as f:
            json.dump(records, f, indent=2)
        print(f"Wrote {len(records)} records to {out_path}")

# Loop through all *_geo_data.json files
for filename in os.listdir(input_dir):
    if filename.endswith("_geo_data.json"):
        state_code = filename.split("_")[0]
        input_path = os.path.join(input_dir, filename)

        process_geo_file(state_code, input_path)
