import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, "..", "..", "data", "spending")
output_dir = os.path.join(script_dir, "..", "..", "data", "spending", "flattened")

years = [
    d for d in os.listdir(input_dir)
    if os.path.isdir(os.path.join(input_dir, d)) and d != "flattened"
]

for year in years:
    year_input_dir = os.path.join(input_dir, year)
    year_output_dir = os.path.join(output_dir, year)
    output_file = os.path.join(year_output_dir, f"{year}_combined.json")
    os.makedirs(year_output_dir, exist_ok=True)

    combined_data = []

    for filename in os.listdir(year_input_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(year_input_dir, filename)
            try:
                with open(file_path, "r") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        combined_data.extend(data)
                    else:
                        print(f"Warning: Skipped {filename} in {year} (not a list)")
            except Exception as e:
                print(f"Error reading {filename} in {year}: {e}")

    with open(output_file, "w") as f:
        json.dump(combined_data, f, indent=2)

    print(f"[{year}] Combined {len(combined_data)} records into {output_file}")
