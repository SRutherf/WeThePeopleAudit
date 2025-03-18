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

def get_dataset(dataset_id, access_key, year, save_path="../../data/bills"):
    """
    Downloads a dataset archive for a given session_id.
    :param dataset_id: The session_id to retrieve
    :param access_key: The access key provided by getDatasetList
    :param year: Year for the dataset to create the correct directory structure
    :param save_path: Base directory where the dataset will be saved
    """
    params = {
        "key": API_KEY,
        "op": "getDataset",
        "id": dataset_id,
        "access_key": access_key
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "dataset" in data:
        dataset_base64 = data["dataset"]
        dataset_zip = base64.b64decode(dataset_base64)
        
        # Ensure save directory exists for the specific year
        year_save_path = os.path.join(save_path, str(year))
        os.makedirs(year_save_path, exist_ok=True)
        
        # Save dataset as ZIP file
        file_path = os.path.join(year_save_path, f"dataset_{dataset_id}_{year}.zip")
        with open(file_path, "wb") as f:
            f.write(dataset_zip)
        
        print(f"Dataset {dataset_id} saved to {file_path}")
        return file_path
    else:
        print("Error downloading dataset:", data)
        return None

# Example Usage
if __name__ == "__main__":
    # Get list of available datasets for Massachusetts
    datasets = get_dataset_list(state="MA")
    
    if datasets:
        print(json.dumps(datasets, indent=2))  # Print dataset info
        
        # Download the first dataset as an example
        first_dataset = datasets[0]
        dataset_id = first_dataset["session_id"]
        access_key = first_dataset["access_key"]
        year = first_dataset.get("year", "unknown_year")  # Get year from dataset info or use a default
        get_dataset(dataset_id, access_key, year)