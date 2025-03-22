import os
import zipfile


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


if __name__ == "__main__":
    # Define the directory containing the zip files
    bills_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "bills")

    # Extract all zip files in the directory
    extract_all_zip_files(bills_directory)