# Using Kaggle Dataset Without Local Download

## Option 1: Use Kaggle Notebooks (Recommended)

Kaggle Notebooks let you work with datasets directly on their cloud platform without downloading.

### Steps:
1. Go to https://www.kaggle.com/datasets/ashley6009/casas-smart-home-dataset
2. Click the **"New Notebook"** button
3. The dataset will be automatically available in the notebook at `/kaggle/input/casas-smart-home-dataset/`
4. Write your code to process, analyze, or extract only the data you need
5. Download only your processed results

### Example Notebook Code:
```python
import pandas as pd
import os

# List all files in the dataset
dataset_path = '/kaggle/input/casas-smart-home-dataset/'
files = os.listdir(dataset_path)
print("Available files:", files)

# Load only the data you need
# Example: df = pd.read_csv(f'{dataset_path}/your_file.csv')

# Process and filter the data
# Save only the results you need
```

## Option 2: Download Specific Files Only

If you need to work locally but only want specific files:

```python
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# List files in the dataset
files = api.dataset_list_files('ashley6009/casas-smart-home-dataset').files
for file in files:
    print(f"File: {file.name}, Size: {file.size}")

# Download only specific files
api.dataset_download_file(
    'ashley6009/casas-smart-home-dataset',
    'specific_file.csv',  # Replace with actual filename
    path='./data/'
)
```

## Benefits of Kaggle Notebooks:
- No local storage needed
- Free GPU/TPU access
- Pre-installed data science libraries
- Easy sharing and collaboration
- Dataset is already unzipped and ready to use
