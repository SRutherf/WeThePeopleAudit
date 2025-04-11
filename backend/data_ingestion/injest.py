import ingest_bills
import ingest_performance
import ingest_spending
import upload_to_s3
import backend.data_processing.unzip_process_bill_data as unzip_process_bill_data

###
# year = 2025
# years = [2025, 2024, ...]
# state = {two digig state code, eg: MA}
# storage = {local, s3}
###
def bills():
    ingest_bills.main(year=2025, state="MA", storage="local")
    unzip_process_bill_data.main()

def peformance():
    ingest_performance.main(states=["geoId/25"])

def spending():
    ingest_spending.main(years=[2024, 2023], state="MA", storage="local")

if __name__ == "__main__":
    print("Starting bill ingestion...")
    bills()
    print("Starting performance ingestion...")
    peformance()
    print("Starting spending ingestion...")
    spending
    print("Uploading to S3...")
    upload_to_s3.main()
