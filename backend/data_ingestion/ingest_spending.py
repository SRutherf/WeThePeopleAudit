import boto3
import calendar
import json
import os
import time
from sodapy import Socrata
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://cthru.data.socrata.com/resource/pegc-naaa.json"
API_KEY = os.getenv("SOCRATA_APP_TOKEN")
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name="us-east-1"
)

def get_latest_create_date():
    """
    Fetches the latest create_date from the Socrata API.
    :return: Sanitized create_date string or raises an exception if no data is found.
    """
    client = Socrata("cthru.data.socrata.com", API_KEY, timeout=60)
    results = client.get("pegc-naaa", limit=1)
    
    if results:
        date = results[0]["create_date"]
        sanitized_date = date.replace(":", "").replace(" ", "_").replace("-", "")
        return sanitized_date
    else:
        raise Exception("No results found through Socrata endpoint.")

def data_already_downloaded(year, month, create_date):
    """
    Checks if the JSON file for the given year, month, and create_date exists.
    :param year: Year of data
    :param month: Month of data
    :param create_date: The create_date from the Socrata API
    :return: Boolean indicating whether the file exists
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(script_dir, "..", "..", "data", "spending")
    year_save_path = os.path.join(save_path, str(year))
    
    expected_filename = f"dataset_{year}_{month:02d}_{create_date}.json"
    expected_file_path = os.path.join(year_save_path, expected_filename)

    return os.path.isfile(expected_file_path)

def get_spending_data(year, month):
    """
    Fetches government spending data for a given state and year using Socrata API.
    :param year: Year for filtering spending data
    :param month: Month for filtering spending data
    :return: JSON of spending records
    """
    client = Socrata("cthru.data.socrata.com", API_KEY, timeout=60)

    start_date = f"{year}-{month:02d}-01T00:00:00.000"
    last_day = calendar.monthrange(year, month)[1]
    end_date = f"{year}-{month:02d}-{last_day}T23:59:59.999"  # Handles up to 28 days, API should handle overflow
    query = f"budget_fiscal_year={year} AND date >= '{start_date}' AND date <= '{end_date}'"
    
    retries=1 # change this number if you have spotty service and might get network errors 
    delay=5
    offset = 0
    limit = 1000
    all_results = []

    # Fetch data, break if no results return or we get less than the limit back
    print(f"Attempting to fetch records for {year}-{month:02d}.  It's gonna take a while...")
    while True:
        for attempt in range(retries):
            # print(f"Getting data for offset {offset}") # uncomment for progress logs if you're interested
            try:
                results = client.get("pegc-naaa", where=query, offset=offset, limit=limit)

                if results:
                    all_results.extend(results)

                    if len(results) < limit:
                        return all_results
                    
                    offset += limit  # Fetch next batch
                    break 
                else:
                    print(f"No data found in attempt {attempt+1}. Retrying...")
                    time.sleep(delay)
            except Exception as e:
                print(f"Error fetching data in attempt {attempt+1}: {e}")
                time.sleep(delay)
        else:
            print(f"Skipping {year}-{month:02d} after {retries} failed attempts.")
            return None

def save_data(year, month, data, create_date, storage):
    """
    Saves the retrieved data to a JSON file.
    :param year: Year of the data
    :param month: Month of the data
    :param data: Retrieved data in JSON format
    :param create_date: The create_date from the Socrata API
    :param stroage: the method for saving the data, either local or hosted on aws.  
    """
    if storage == "local":
        script_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(script_dir, "..", "..", "data", "spending")

        year_save_path = os.path.join(save_path, str(year))
        os.makedirs(year_save_path, exist_ok=True)

        file_path = os.path.join(year_save_path, f"dataset_{year}_{month:02d}_{create_date}.json")
        
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=2)

        print(f"Spending data for {year} saved to {file_path}")
        return file_path
    
    elif storage == "s3":
        # Prepare to upload to S3
        s3_key = f"spending/{year}/dataset_{year}_{month:02d}_{create_date}.json"
        s3_client.put_object(Bucket=S3_BUCKET, Key=s3_key, Body=json.dumps(data).encode('utf-8'))
        print(f"Spending data for {year} uploaded to s3://{S3_BUCKET}/{s3_key}")
        return s3_key
    
    else:
        print("Invalid storage option, dummy.")

def main(years, storage):
    # [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010] # all years available from scrota
    # [2024, 2023] # years for the last full general session, #193
    try:
        create_date = get_latest_create_date()
        print(f"Latest create_date: {create_date}")

        for year in years:
            for month in range(1, 13):
                if storage == "s3" or not data_already_downloaded(year, month, create_date):
                    print(f"Fetching data for {year}-{month:02d}")
                    spending_data = get_spending_data(year, month)
                    
                    if spending_data:
                        save_data(year, month, spending_data, create_date, storage)
                    else:
                        print(f"No data retrieved for {year}-{month:02d}. Skipping.")
                else:
                    print(f"Data for {year}-{month:02d} already exists. Skipping download.")
    except Exception as e:
            print(f"Error occurred: {e}")