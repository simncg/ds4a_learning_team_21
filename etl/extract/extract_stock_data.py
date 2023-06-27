# Set working directory and import libraries 
import os
import sys
import time 
import pandas as pd
import requests.exceptions
import datetime
import json
from geopy.geocoders import ArcGIS
from yahooquery import Ticker


sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
from src.data import stock_data
from src.utils.date_json_handler import date_handler

class DataExtractor:
    def __init__(self, symbols):
        self.symbols = symbols
        self.symbols_without_location = []
        self.symbols_with_location = []
    
    def __extract_financial_price_data(self, symbol):
        data = stock_data.StockData(symbol)
        data.scrape_financial_statements()
        data.retrieve_profile_stock_price(start="2017-01-01", end=datetime.date.today().isoformat())
        data.save_to_json()

    def __extract_location(self):
        geolocator = ArcGIS()
        self.symbols_without_location = []
        self.symbols_with_location = []
        
        for symbol in self.symbols:
            with open(os.path.join('../../data/raw/json_data', symbol + ".json")) as f:
                data = json.load(f)["profile"]
                # Invalid Files: No data/address found.
                if type(data) == str:
                    print(f"NO DATA FOUND FOR: {symbol}. Message: {data}")
                    self.symbols_without_location.append(symbol)
                    continue
                        
                elif "address1" not in data:
                    print(f"NO ADDRESS FOUND FOR: {symbol}. Message: {data}")
                    self.symbols_without_location.append(symbol)
                    continue
                        
                # Valid Files
                self.symbols_with_location.append(symbol)
                
                # Street Address
                address = ""
                address += data["address1"] + " " if "address1" in data else ''
                address += data["city"] + " " if "city" in data else ''
                address += data["state"] + " " if "state" in data else ''
                address += data["zip"] + " " if "zip" in data else ''
                address += data["country"] if "country" in data else ''

                # Get location 
                location = geolocator.geocode(address)

                # If location is not found, add missing value and skip
                if location is None:
                    print(f"NO LOCATION FOUND FOR: {symbol}")
                    self.symbols_without_location.append(symbol)
                    data["latitude"] = None 
                    data["longitude"] = None
                else:
                    # Add Latitude & Longitude
                    data["latitude"] = location.latitude
                    data["longitude"] = location.longitude
                    self.symbols_with_location.append(symbol)
                    
                # Save to JSON
                with open(os.path.join('../../data/raw/json_data', symbol + ".json"), 'w') as outfile:
                    json.dump(data, outfile)
                    
        
        print(f"\nUnable to geocode {len(self.symbols_without_location)} locations: {self.symbols_without_location} ")
        print(f"\nAble to geocode {len(self.symbols_with_location)} locations: {self.symbols_with_location} ")
        

    # Method to compare 2 dictionaries (old company profile dictionary vs new company profile dictionary)
    def __sync_dicts(self, dict1, dict2):
        # iterate over all keys in the second dict
        for key in dict2.keys():
            # Skip 'latitude' and 'longitude'
            if key in ['latitude', 'longitude']:
                continue
            
            # If the key is in dict1 and the values are not the same
            if key in dict1 and dict1[key] != dict2[key]:
                # Update the value in dict1
                dict1[key] = dict2[key]
        return dict1

    
    # Update data that already exists
    def __update_stock_price_and_profile(self, symbol):
        with open("../../data/raw/json_data/" + symbol +".json", 'r') as f:
            data = json.load(f)
            stock_data = pd.DataFrame(data["stock_price"])    
            stock_profile = data["profile"]
            
        if stock_data["date"].max() < datetime.date.today().isoformat():
            # Max date in data
            max_date = datetime.datetime.strptime(stock_data["date"].max(), "%Y-%m-%d").date()
            
            # Start date of data to be downloaded
            start = (max_date + datetime.timedelta(days=1)).isoformat()
            
            # End date of data to be downloaded
            end = datetime.date.today().isoformat()
            
            # Retrieve data from Yahoo Finance
            sym = Ticker(symbol)
                    
            # Obtain stock data
            new_stock_data = sym.history(start=start, end=end).reset_index()
            
            # Append with previous stock data 
            stock_data = pd.concat([stock_data, new_stock_data], axis = 0)
            
            # Get company profile 
            new_profile = sym.asset_profile[symbol]
            
            # Update profile 
            updated_profile = self.__sync_dicts(stock_profile, new_profile)
            
            # Save CSV file 
            stock_data.to_csv(f"../data/raw/stock_prices/{symbol}.csv", index = False)
            
            # Save company profile as JSON
            with open(f"../data/raw/company_profile/{symbol}.json", 'w') as f:
                json.dump(updated_profile, f)
                
            # Update JSON file with all info 
            data["stock_price"] = stock_data
            data["profile"] = updated_profile
            
            with open(f"../data/raw/json_data/{symbol}.json", 'w') as f:
                json.dump(data, f, default=date_handler)
        
        
    
    def extract_all_symbols(self):
        
        symbols_available = [file.replace(".json", "")  for file in os.listdir('../../data/raw/json_data')]
        
        # Define the maximum number of retries
        max_retries = 3
        
        # Iterate over the symbols
        for symbol in self.symbols:
            print(symbol)
            # If the data is already available 
            if symbol in symbols_available:
                # Update stock price and profile data
                self.__update_stock_price_and_profile(symbol)
                                                
            else:
                retries = 0
                while retries < max_retries:
                    try:
                        time.sleep(5)
                        self.__extract_financial_price_data(symbol)
                        break  # If everything is successful, break the loop and move to the next symbol
                    except requests.exceptions.RequestException as e:
                        print(f"A connection error occurred: {e}")
                        retries += 1
                        print(f"Retrying ({retries}/{max_retries}) in 5 minutes...")
                        time.sleep(300)
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        break  # Move to the next symbol for other types of exceptions
                if retries == max_retries:
                    print(f"Max retries reached for symbol {symbol}. Moving to the next symbol...")

                
        # Extract latitude and longitude for all symbols
        self.__extract_location()  




# %%


"""
with open("../../data/raw/json_data/JPM.json", 'r') as f:
    data = json.load(f)
    stock_data = pd.DataFrame(data["stock_price"])    
    stock_profile = data["profile"]


symbol = "JPM"


def sync_dicts(dict1, dict2):
    # iterate over all keys in the second dict
    for key in dict2.keys():
        # Skip 'latitude' and 'longitude'
        if key in ['latitude', 'longitude']:
            continue
            
        # If the key is in dict1 and the values are not the same
        if key in dict1 and dict1[key] != dict2[key]:
            # Update the value in dict1
            dict1[key] = dict2[key]
    return dict1

# %%
from yahooquery import Ticker

if stock_data["date"].max() < datetime.date.today().isoformat():
    
    # Max date in data
    max_date = datetime.datetime.strptime(stock_data["date"].max(), "%Y-%m-%d").date()
    
    # Start date of data to be downloaded
    start = (max_date + datetime.timedelta(days=1)).isoformat()
    
    # End date of data to be downloaded
    end = datetime.date.today().isoformat()
    
    # Retrieve data from Yahoo Finance
    sym = Ticker(symbol)
            
    # Obtain stock data
    new_stock_data = sym.history(start=start, end=end).reset_index()
    
    # Append with previous stock data 
    stock_data = pd.concat([stock_data, new_stock_data], axis = 0)
    
    # Get company profile 
    new_profile = sym.asset_profile[symbol]
    
    updated_profile = sync_dicts(stock_profile, new_profile)
     

"""


    
    
    
# %%
