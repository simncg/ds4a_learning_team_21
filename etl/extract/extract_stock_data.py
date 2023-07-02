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
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data")
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
from src.data import stock_data
from src.utils.date_json_handler import date_handler


class DataExtractor:
    def __init__(self, symbols: list):
        self.symbols = symbols
    
    def __extract_financial_price_data(self, symbol):
        data = stock_data.StockData(symbol)
        data.scrape_financial_statements()
       # data.retrieve_profile_stock_price(start="2017-01-01", end=datetime.date.today().isoformat())
        data.retrieve_profile_stock_price(start="2017-01-01", end="2022-03-30")
        data.save_to_json()

    def __extract_location(self, symbol):
        geolocator = ArcGIS()
        
        with open(os.path.join(DATA_PATH, "raw", "json_data", f"{symbol}.json"), 'r') as f:
            all_data = json.load(f)
            data = all_data["profile"]
            # Invalid Files: No data/address found.
        if type(data) == str:
            return False
                    
        elif "address1" not in data:
            return False
                    
        # Street Address
        address = ""
        address += data["address1"] + " " if "address1" in data else ''
        address += data["city"] + " " if "city" in data else ''
        address += data["state"] + " " if "state" in data else ''
        address += data["zip"] + " " if "zip" in data else ''
        address += data["country"] if "country" in data else ''

        # Get location 
        location = geolocator.geocode(address)

        # If location is not found, add missing value and return False
        if location is None:
            data["latitude"] = None 
            data["longitude"] = None
            return False
        else:
            # Add Latitude & Longitude
            data["latitude"] = location.latitude
            data["longitude"] = location.longitude
        
        all_data["profile"] = data
                
        # Save to JSON
        with open(os.path.join(DATA_PATH, "raw", "json_data", f"{symbol}.json"), 'w') as outfile:
            json.dump(all_data, outfile)

        return True
    
    # Update stock data 
    def __update_stock_data(self, symbol):
        with open(os.path.join(DATA_PATH, "raw", "json_data", f"{symbol}.json"), 'r') as f:
            data = json.load(f)

        stock_data = pd.DataFrame(data["stock_price"]) 

        if stock_data.empty:
            print(f"No stock data found for symbol {symbol}.")
            return
         
        stock_data["date"] = pd.to_datetime(stock_data["date"]).dt.date

            
        if stock_data["date"].max() < datetime.date.today():
    
            # Start date of data to be downloaded
            start = (stock_data["date"].max() + datetime.timedelta(days=1)).isoformat()
                    
            # End date of data to be downloaded
            end = datetime.date.today().isoformat()
                    
            # Retrieve data from Yahoo Finance
            sym = Ticker(symbol)
                            
            # Obtain stock data
            new_stock_data = sym.history(start=start, end=end).reset_index()

            # If there is no new stock data, finish the task
            if new_stock_data.empty:
                print(f"Not new stock data available in Yahoo Finance API for {symbol}")
                return 

            new_stock_data["date"] = pd.to_datetime(new_stock_data["date"]).dt.date
                    
            # Append with previous stock data 
            stock_data = pd.concat([stock_data, new_stock_data], axis = 0)
            stock_data = stock_data.reset_index(drop=True)
            stock_data["date"] = pd.to_datetime(stock_data["date"]).dt.date

            # Save CSV file 
            stock_data.to_csv(os.path.join(DATA_PATH, "raw", "stock_prices", f"{symbol}.csv"), index=False)

            #print(stock_data["date"].min())
            #print("Data updated until " + stock_data["date"].max() + "for " + symbol)

            # Update JSON file with all info 
            data["stock_price"] = stock_data.to_dict()

            # Save to JSON
            with open(os.path.join(DATA_PATH, "raw", "json_data", f"{symbol}.json"), 'w') as outfile:
                json.dump(data, outfile, default=date_handler)
        else: 
            print(f"Stock data for {symbol} is already up to date.")
            return 

        
        
    def extract_data(self):
        
        symbols_available = [file.replace(".json", "")  for file in os.listdir(os.path.join(DATA_PATH, "raw", "json_data"))]
        
        # Define the maximum number of retries
        max_retries = 3
        
        # Iterate over the symbols
        for symbol in self.symbols:
            print(symbol)
            # If the data is already available 
            if symbol in symbols_available:
                # Update stock price
                self.__update_stock_data(symbol)

            else:
                retries = 0
                while retries < max_retries:
                    try:
                        time.sleep(5)
                        # Extract stock price and financial data
                        self.__extract_financial_price_data(symbol)

                        # Extract location 
                        self.__extract_location(symbol)

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
                        
    