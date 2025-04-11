import json
import os
from glob import glob

# Base directories
script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, "..", "..", "data", "bills")
output_dir = os.path.join(script_dir, "..", "..", "data", "bills", "flattened")

# Get all year folders under bills/ (excluding 'flattened')
years = [
    d for d in os.listdir(input_dir)
    if os.path.isdir(os.path.join(input_dir, d)) and d != "flattened"
]

# The types of data to process
data_types = ["bill", "people", "vote"]

for year in years:
    year_input_dir = os.path.join(input_dir, year)

    for data_type in data_types:
        combined_data = []

        # Find matching files like */*/*/{type}/*.json
        data_files = glob(os.path.join(year_input_dir, "*", "*", "*", data_type, "*.json"))

        for file_path in data_files:
            try:
                with open(file_path, "r") as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        combined_data.append(data)
                    else:
                        print(f"Warning: Skipped {file_path} (not a dict)")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

        # Define output path and save
        type_output_dir = os.path.join(output_dir, data_type, year)
        os.makedirs(type_output_dir, exist_ok=True)

        output_file = os.path.join(type_output_dir, f"{year}_combined.json")
        with open(output_file, "w") as f:
            json.dump(combined_data, f, indent=2)

        print(f"[{year}] {data_type}: Combined {len(combined_data)} records into {output_file}")
