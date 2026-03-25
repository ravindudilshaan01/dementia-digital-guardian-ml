import os
from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi

# Load API credentials
load_dotenv()

# Initialize and authenticate
api = KaggleApi()
api.authenticate()

print("Fetching dataset file list...")
print("=" * 60)

# List all files in your dataset
dataset = 'ashley6009/casas-smart-home-dataset'
files = api.dataset_list_files(dataset).files

print(f"\nDataset: {dataset}")
print(f"Total files: {len(files)}\n")

# Display file information
for i, file in enumerate(files, 1):
    size_mb = file.size / (1024 * 1024)  # Convert to MB
    print(f"{i}. {file.name}")
    print(f"   Size: {size_mb:.2f} MB")
    print()

print("=" * 60)
print("\nNext steps:")
print("1. Work directly in Kaggle Notebooks (recommended)")
print("   Visit: https://www.kaggle.com/datasets/ashley6009/casas-smart-home-dataset")
print("   Click 'New Notebook'")
print("\n2. Or download specific files only using download_specific_file.py")
