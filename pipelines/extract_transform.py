import os
import sys
import time 
import pandas as pd
sys.path.append(os.path.dirname(os.getcwd()))
from etl.extract import extract_stock_data
from etl.transform import transform_data

# Read data with companies symbols
symbols = pd.read_excel("../data/raw/financial_sector_companies.xlsx")["Symbol"].to_list()

#%%

# Use Extractor class, instantiate the class with all financial sector companies
Extractor = extract_stock_data.DataExtractor(symbols)

# Extract all data from Yahoo Finance and Stock Data Webpage. If data already exists, just update stock data.
Extractor.extract_data()

#%%            
# Transform data (clean data) and save transformed data to CSV files
Transformer = transform_data.FinancialDataTransformer(symbols)
Transformer.transform()
Transformer.save_to_csv()