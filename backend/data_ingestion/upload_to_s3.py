import boto3
import os
from dotenv import load_dotenv

load_dotenv()
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name="us-east-1"
)

def upload_flattened_bill_data_to_s3(flattened_root):
    folders_to_upload = ['bill', 'people', 'vote']

    for folder in folders_to_upload:
        folder_path = os.path.join(flattened_root, folder)
        if not os.path.exists(folder_path):
            continue

        for year in os.listdir(folder_path):
            year_dir = os.path.join(folder_path, year)
            if os.path.isdir(year_dir):
                json_filename = f"{year}_combined.json"
                json_path = os.path.join(year_dir, json_filename)

                if os.path.exists(json_path):
                    s3_key = f"bills/{year}/{folder}/{json_filename}"
                    s3_client.upload_file(json_path, S3_BUCKET, s3_key)
                    print(f"Uploaded {json_path} to s3://{S3_BUCKET}/{s3_key}")
                else:
                    print(f"Missing file: {json_path}")

def upload_flattened_spending_data_to_s3(flattened_root):
    for year in os.listdir(flattened_root):
        year_dir = os.path.join(flattened_root, year)
        if os.path.isdir(year_dir):
            json_filename = f"{year}_combined.json"
            json_path = os.path.join(year_dir, json_filename)

            if os.path.exists(json_path):
                s3_key = f"spending/{year}/{json_filename}"
                s3_client.upload_file(json_path, S3_BUCKET, s3_key)
                print(f"Uploaded {json_path} to s3://{S3_BUCKET}/{s3_key}")
            else:
                print(f"Missing file: {json_path}")

def upload_flattened_performance_data_to_s3(flattened_root):
    for file in os.listdir(flattened_root):
        if file.endswith(".json"):
            file_path = os.path.join(flattened_root, file)
            target_folder = "perf" if "_perf_data.json" in file else "geo"
            s3_key = f"performance/{target_folder}/{file}"
            s3_client.upload_file(file_path, S3_BUCKET, s3_key)
            print(f"Uploaded {file_path} to s3://{S3_BUCKET}/{s3_key}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    bills_flattened_dir = os.path.join(base_dir, "..", "..", "data", "bills", "flattened")
    spending_flattened_dir = os.path.join(base_dir, "..", "..", "data", "spending", "flattened")
    performance_dir = os.path.join(base_dir, "..", "..", "data", "performance", "states_transformed")

    upload_flattened_bill_data_to_s3(bills_flattened_dir)
    upload_flattened_spending_data_to_s3(spending_flattened_dir)
    upload_flattened_performance_data_to_s3(performance_dir)

if __name__ == "__main__":
    main()
