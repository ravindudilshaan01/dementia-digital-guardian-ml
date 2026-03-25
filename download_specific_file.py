import os
from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi

# Load API credentials
load_dotenv()

# Initialize and authenticate
api = KaggleApi()
api.authenticate()

# Configuration
dataset = 'ashley6009/casas-smart-home-dataset'
file_name = 'YOUR_FILE_NAME_HERE.csv'  # Replace with actual filename
output_path = './data/'

# Create output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

print(f"Downloading specific file: {file_name}")
print(f"From dataset: {dataset}")
print(f"To: {output_path}")
print("=" * 60)

try:
    api.dataset_download_file(
        dataset,
        file_name,
        path=output_path
    )
    print(f"\n[SUCCESS] File downloaded to: {output_path}{file_name}")

except Exception as e:
    print(f"\n[FAILED] Error: {e}")
    print("\nTip: Run list_dataset_files.py first to see available files")
