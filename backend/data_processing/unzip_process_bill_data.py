import json
import os
import zipfile

def extract_all_zip_files(directory):
    """
    Extracts all zip files in the specified directory and its subdirectories,
    then processes relevant JSON files using prep_data_for_databricks.
    :param directory: The directory to search for zip files.
    """
    folders_to_process = ['bill', 'people', 'vote']

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):
                zip_path = os.path.join(root, file)
                extract_path = os.path.join(root, os.path.splitext(file)[0])

                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)

                print(f"Extracted {zip_path} to {extract_path}")

                for sub_root, sub_dirs, _ in os.walk(extract_path):
                    for folder in folders_to_process:
                        folder_path = os.path.join(sub_root, folder)
                        if os.path.exists(folder_path):
                            for json_file in os.listdir(folder_path):
                                if json_file.endswith(".json"):
                                    file_path = os.path.join(folder_path, json_file)
                                    prep_data_for_databricks(folder, file_path)

def prep_data_for_databricks(folder, filepath):
    key_mapping = {
        "bill": "bill",
        "people": "person",
        "vote": "roll_call"
    }
    key = key_mapping.get(folder)

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {filepath}: {e}")
        return False

    if key not in data:
        print(f"Expected key '{key}' not found in {filepath}. Should exist in unzipped data.")
        return False

    inner_data = data[key]

    with open(filepath, 'w') as f:
        json.dump(inner_data, f)

    return True            

def main():
    bills_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "bills")
    extract_all_zip_files(bills_directory)