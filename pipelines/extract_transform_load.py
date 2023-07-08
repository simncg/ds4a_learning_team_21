import os
import sys
import time 
import pandas as pd
sys.path.append(os.path.dirname(os.getcwd()))
from etl.extract import extract_stock_data
from etl.transform import transform_data
from etl.load import load_data

# Read data with companies symbols
symbols = pd.read_excel("../data/raw/financial_sector_companies.xlsx")["Symbol"].to_list()

#--------------------------------#
#       1. Extract  Data         #
#--------------------------------#

# Use Extractor class, instantiate the class with all financial sector companies
Extractor = extract_stock_data.DataExtractor(symbols)

# Extract all data from Yahoo Finance and Stock Data Webpage. If data already exists, just update stock data.
Extractor.extract_data()

#---------------------------------#
#       2. Transform Data         #
#---------------------------------#            

# Transform data (clean data) and save transformed data to CSV files
Transformer = transform_data.FinancialDataTransformer(symbols)
Transformer.transform()
Transformer.save_to_csv()

#-------------------------------#
#          3. Load Data         #
#-------------------------------#     


# 3.1 LOAD DATA TO S3 ---------------

# Load data to 
bucket_name = "learning-team-21"
folder_processed = 'processed'
folder_raw_data = 'raw'

# Instantiate the class
s3_loader = load_data.DataLoader()

# Create bucket 
s3_loader.create_bucket(bucket_name)

# Create folders in the bucket
s3_loader.create_folder(bucket_name, folder_raw_data)
s3_loader.create_folder(bucket_name, folder_processed)

# Upload json files (raw data) to the S3 bucket
for file in os.listdir("../../data/raw/json_data"):
    if file.endswith(".json"):
        print(file)
        s3_loader.upload_file('../../data/raw/json_data/'+file, bucket_name, folder_raw_data+'/'+file)

# Upload processed data to the S3 bucket
for file in os.listdir('../../data/processed'):
    if file.endswith(".csv"):
        print(file)
        s3_loader.upload_file('../../data/processed/'+ file, bucket_name, folder_processed+'/'+file)

