import os
import kagglehub
import pandas as pd
from dotenv import load_dotenv

# Load API key from .env file (never hardcode it)
load_dotenv()
os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

print(f"Authenticated as: {os.getenv('KAGGLE_USERNAME')}")

try:
    # Download the dataset first
    print("Downloading dataset...")
    dataset_path = kagglehub.dataset_download("ashley6009/casas-smart-home-dataset")
    print(f"Dataset downloaded to: {dataset_path}")

    # List available files
    import glob
    files = glob.glob(os.path.join(dataset_path, "*"))
    print("Available files:")
    for file in files:
        file_name = os.path.basename(file)
        file_size = os.path.getsize(file)
        print(f"  - {file_name} ({file_size:,} bytes)")

    # Load the first CSV file found
    csv_files = glob.glob(os.path.join(dataset_path, "*.csv"))
    if csv_files:
        csv_file = csv_files[0]
        print(f"\nLoading: {os.path.basename(csv_file)}")
        df = pd.read_csv(csv_file)

        print("Shape:", df.shape)
        print("Columns:", df.columns.tolist())
        print("\nFirst 5 rows:")
        print(df.head())

        print("\nDataset info:")
        print(df.info())

    else:
        print("No CSV files found in the dataset.")
        # Try other file types
        other_files = [f for f in files if not f.endswith('.csv')]
        if other_files:
            print("Other files available:")
            for file in other_files:
                print(f"  - {os.path.basename(file)}")

except Exception as e:
    print(f"Error: {e}")
    print("\nTroubleshooting steps:")
    print("1. Make sure your Kaggle API key is valid and has the right permissions")
    print("2. Check if the dataset requires consent - visit the dataset page on Kaggle")
    print("3. Ensure the dataset exists and is publicly accessible")
    print("4. Try visiting: https://www.kaggle.com/datasets/ashley6009/casas-smart-home-dataset")