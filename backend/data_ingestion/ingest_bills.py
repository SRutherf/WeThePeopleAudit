
import base64
import boto3
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://api.legiscan.com/"
API_KEY = os.getenv("LEGISCAN_API_KEY")
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name="us-east-1"
)

def get_dataset_list(year=None, state=None):
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

def get_dataset(session_id, access_key, dataset_date, year, storage):
    """
    Downloads a dataset archive for a given session_id.
    :param session_id: The session_id to retrieve
    :param access_key: The access key provided by getDatasetList
    :param year: Year for the dataset to create the correct directory structure
    :param dataset_date: Date of the dataset to include in filename
    :param stroage: the method for saving the data, either local or hosted on aws.  
    :return: Zip file with folders for bills, people, and votes
    """
    sanitized_date = dataset_date.replace("-", "")
    file_name = f"dataset_{session_id}_{year}_{sanitized_date}.zip"
    
    if storage == "local":
        script_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(script_dir, "..", "..", "data", "bills", str(year))
        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, file_name)
        
        if os.path.exists(file_path):
            print(f"Dataset {session_id} for {year} on {dataset_date} already exists. Skipping download.")
            return None
    else:
        file_path = file_name
    
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
            
            if storage == "local":
                with open(file_path, "wb") as f:
                    f.write(dataset_zip)
                print(f"Dataset {session_id} saved to {file_path}")
            elif storage == "s3":
                s3_key = f"bills/{year}/{file_name}"
                s3_client.put_object(Bucket=S3_BUCKET, Key=s3_key, Body=dataset_zip)
                print(f"Dataset {session_id} uploaded to s3://{S3_BUCKET}/{s3_key}")
            return file_path
        else:
            print("Error: 'zip' key missing or invalid inside 'dataset'.")
    else:
        print("Error: 'dataset' key missing or invalid in response.")
    
    return None

def main(year, state, storage):
    datasets = get_dataset_list(year=year, state=state)
    
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
            get_dataset(session_id, access_key, dataset_date, year=year, storage=storage)