import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, "..", "..", "data", "performance", "states_raw")
output_dir = os.path.join(script_dir, "..", "..", "data", "performance", "states_transformed")

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith("_perf_data.json"):

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        with open(input_path, "r") as f:
            raw_data = json.load(f)

        transformed = []
        for dcid, metrics in raw_data.items():
            row = {"dcid": dcid}
            for metric_name, metric in metrics.items():
                if not isinstance(metric, dict):
                    print(f"Warning: skipping {metric_name} in {dcid} (not a dict)")
                    continue
                row[metric_name] = {
                    "data": metric.get("data", {}),
                    "source": metric.get("source"),
                    "unit": metric.get("unit")
                }
            transformed.append(row)

        # Save to output path
        with open(output_path, "w") as f:
            json.dump(transformed, f, indent=2)

        print(f"Processed {filename}")