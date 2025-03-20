import time
import os
import json
import calendar
from sodapy import Socrata
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("SOCRATA_APP_TOKEN")
BASE_URL = "https://cthru.data.socrata.com/resource/pegc-naaa.json"

def get_latest_create_date():
    """
    Fetches the latest create_date from the Socrata API.
    :return: Sanitized create_date string or raises an exception if no data is found.
    """
    client = Socrata("cthru.data.socrata.com", API_KEY, timeout=10)
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
    
    retries=3 
    delay=5
    offset = 0
    limit = 1000
    all_results = []

    # Fetch data, break if no results return or we get less than the limit back
    while True:
        for attempt in range(retries):
            try:
                print(f"Attempt {attempt+1} at fetching records from offset {offset}")
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

def save_data(year, month, data, create_date):
    """
    Saves the retrieved data to a JSON file.
    :param year: Year of the data
    :param data: Retrieved data in JSON format
    """
    # Do this so python doesnt use its own bullshit relative path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(script_dir, "..", "..", "data", "spending")

    year_save_path = os.path.join(save_path, str(year))
    os.makedirs(year_save_path, exist_ok=True)

    file_path = os.path.join(year_save_path, f"dataset_{year}_{month:02d}_{create_date}.json")
    
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=2)

    print(f"Spending data for {year} saved to {file_path}")
    return file_path

if __name__ == "__main__":
    year = 2025
    try:
        create_date = get_latest_create_date()
        print(f"Latest create_date: {create_date}")

        for month in range(1, 13):
            if not data_already_downloaded(year, month, create_date):
                print(f"Fetching data for {year}-{month:02d}")
                spending_data = get_spending_data(year, month)
                
                if spending_data:
                    save_data(year, month, spending_data, create_date)
                else:
                    print(f"No data retrieved for {year}-{month:02d}. Skipping.")
            else:
                print(f"Data for {year}-{month:02d} already exists. Skipping download.")
    except Exception as e:
            print(f"Error occurred: {e}")