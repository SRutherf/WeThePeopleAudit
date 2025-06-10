from backend.data_ingestion import ingest_bills, ingest_performance, ingest_spending, upload_to_s3
from backend.data_processing import unzip_process_bill_data

###
# year = 2025
# years = [2025, 2024, ...]
# state = {two digig state code, eg: MA}
# storage = {local, s3}
###
def bills():
    ingest_bills.main(year=[2020, 2021, 2022, 2023, 2024], state="MA", storage="local")
    unzip_process_bill_data.main()

def peformance():
    ingest_performance.main(states=["geoId/25"])

def spending():
    ingest_spending.main(years=[2020, 2021, 2022], storage="local")

def upload():
    upload_to_s3.main()

if __name__ == "__main__":
    # print("Starting bill ingestion...")
    # bills()
    # print("Starting performance ingestion...")
    # peformance()
    print("Starting spending ingestion...")
    spending()
    # print("Uploading to S3...")
    # upload()
