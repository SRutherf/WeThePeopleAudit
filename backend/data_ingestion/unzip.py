import boto3
import os
import zipfile
from dotenv import load_dotenv

load_dotenv()
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name="us-east-2"
)

def extract_all_zip_files(directory):
    """
    Extracts all zip files in the specified directory and its subdirectories.
    :param directory: The directory to search for zip files.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):
                zip_path = os.path.join(root, file)
                extract_path = os.path.join(root, os.path.splitext(file)[0])

                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)

                print(f"Extracted {zip_path} to {extract_path}")
                upload_to_s3(extract_path)

def upload_to_s3(extract_path):
    """
    Uploads folders from the extracted directory to S3.
    :param directory: Path to the extracted files.
    """
    year = os.path.basename(os.path.dirname(extract_path))
    base_folder_name = os.path.basename(extract_path)
    s3_key_base_path = f"bills/{year}/{base_folder_name}"
    parent_folder = os.path.dirname(extract_path)

    folders_to_upload = ['bill', 'people', 'vote']

    for root, dirs, files in os.walk(parent_folder):
        for dir_name in dirs:
            target_path = os.path.join(root, dir_name)
            for folder in folders_to_upload:
                folder_path = os.path.join(target_path, folder)
                if os.path.exists(folder_path):
                    for json_file in os.listdir(folder_path):
                        if json_file.endswith(".json"):
                            file_path = os.path.join(folder_path, json_file)
                            s3_key = f"{s3_key_base_path}/{folder}/{json_file}"

                            s3_client.upload_file(file_path, S3_BUCKET, s3_key)
                            print(f"Uploaded {file_path} to s3://{S3_BUCKET}/{s3_key}")             

if __name__ == "__main__":
    # Define the directory containing the zip files
    bills_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "bills")

    # Extract all zip files in the directory
    extract_path = extract_all_zip_files(bills_directory)