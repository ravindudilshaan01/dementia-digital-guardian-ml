import os
from dotenv import load_dotenv
import kagglehub

# Load API credentials
load_dotenv()
os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

print("Testing Kaggle API connection...")
print(f"Username: {os.getenv('KAGGLE_USERNAME')}")

# Test with a simple, public dataset that shouldn't require consent
try:
    print("\n1. Testing with a simple public dataset...")
    test_path = kagglehub.dataset_download("heptapod/titanic")
    print(f"[SUCCESS] Test dataset downloaded to: {test_path}")
    print("Your API credentials are working correctly.")

except Exception as e:
    print(f"[FAILED] API test failed: {e}")
    print("Check your API credentials in the .env file.")
    exit(1)

# Now try your dataset
try:
    print("\n2. Testing your specific dataset...")
    dataset_path = kagglehub.dataset_download("ashley6009/casas-smart-home-dataset")
    print(f"[SUCCESS] Your dataset downloaded to: {dataset_path}")

except Exception as e:
    print(f"[FAILED] Your dataset failed: {e}")
    print("\nNext steps:")
    print("1. Visit: https://www.kaggle.com/datasets/ashley6009/casas-smart-home-dataset")
    print("2. Make sure you're logged in with username: ashley6009")
    print("3. Accept any terms of use or consent requirements")
    print("4. Ensure the dataset is public (not private)")
    print("5. Try running this test again")