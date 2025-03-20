import os
import requests
import json
import base64
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("LEGISCAN_API_KEY")
BASE_URL = "https://api.legiscan.com/"

def get_dataset_list(state=None, year=None):
    """
    Fetches the list of available session datasets.
    :param state: (Optional) Filter results by state abbreviation (e.g. 'MA')
    :param year: (Optional) Filter results by year (e.g., 2025)
    :return: List of dataset metadata
    """
    params = {"key": API_KEY, "op": "getDatasetList"}
    if state:
        params["state"] = state
    if year:
        params["year"] = year
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if "datasetlist" in data:
        return data["datasetlist"]
    else:
        print("Error fetching dataset list:", data)
        return None

def get_dataset(session_id, access_key, year, dataset_date):
    """
    Downloads a dataset archive for a given session_id.
    :param session_id: The session_id to retrieve
    :param access_key: The access key provided by getDatasetList
    :param year: Year for the dataset to create the correct directory structure
    :param dataset_date: Date of the dataset to include in filename
    :return: Zip file with folders for bills, people, and votes
    """
    # Do this so python doesnt use its own bullshit relative path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(script_dir, "..", "..", "data", "bills")

    year_save_path = os.path.join(save_path, str(year))
    os.makedirs(year_save_path, exist_ok=True)

    sanitized_date = dataset_date.replace("-", "")
    file_path = os.path.join(year_save_path, f"dataset_{session_id}_{year}_{sanitized_date}.zip")

    if os.path.exists(file_path):
        print(f"Dataset {session_id} for {year} on {dataset_date} already exists. Skipping download.")
        return None
    
    params = {
        "key": API_KEY,
        "op": "getDataset",
        "id": session_id,
        "access_key": access_key
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "dataset" in data and isinstance(data["dataset"], dict):
        dataset_info = data["dataset"]
        
        if "zip" in dataset_info and isinstance(dataset_info["zip"], str):
            try:
                dataset_zip = base64.b64decode(dataset_info["zip"])
            except Exception as e:
                print(f"Error decoding base64 dataset: {e}")
                return None
            
            with open(file_path, "wb") as f:
                f.write(dataset_zip)
            
            print(f"Dataset {session_id} saved to {file_path}")
            return file_path
        else:
            print("Error: 'zip' key missing or invalid inside 'dataset'.")
    else:
        print("Error: 'dataset' key missing or invalid in response.")
    
    return None

if __name__ == "__main__":
    datasets = get_dataset_list(state="MA")
    
    if datasets:
        for dataset in datasets:
            print(json.dumps({
                "session_name": dataset.get("session_name"),
                "dataset_date": dataset.get("dataset_date"),
                "session_id": dataset.get("session_id"),
                "access_key": dataset.get("access_key")
            }, indent=2))

        # Download all datasets
        for dataset in datasets:
            session_id = dataset["session_id"]
            access_key = dataset["access_key"]
            year = dataset["year_start"]
            dataset_date = dataset["dataset_date"]
            get_dataset(session_id, access_key, year, dataset_date)