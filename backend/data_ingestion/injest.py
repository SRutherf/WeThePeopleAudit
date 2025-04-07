import ingest_bills
import ingest_spending
import unzip_upload

###
# year = 2025
# years = [2025, 2024, ...]
# state = {two digig state code, eg: MA}
# storage = {local, s3}
###
def bills():
    ingest_bills.main(year=2025, state="MA", storage="local")
    unzip_upload.main()

def peformance():
    print("TODO: Implement performance ingestion")

def spending():
    ingest_spending.main(years=[2024, 2023], state="MA", storage="s3")

if __name__ == "__main__":
    unzip_upload.main()
    # print("Starting bill ingestion...")
    # bills()
    # print("Starting performance ingestion...")
    # peformance()
    # print("Starting spending ingestion...")
    # spending
