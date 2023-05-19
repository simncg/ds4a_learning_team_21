import pandas as pd
from bs4 import BeautifulSoup
import requests
from yahooquery import Ticker
import json
import datetime
from ..utils.date_json_handler import date_handler


class StockData:
    """
    Class to scrape and retrieve stock data and related financial data of a company.
    
    Attributes
    ----------
    symbol : str
        The stock symbol of the company.
    urls : dict
        A dictionary of URLs for scraping financial data.
    company_data : dict
        A dictionary containing all scraped and retrieved data.
    scrape_done : bool
        A flag indicating if data scraping is completed.
    retrieve_done : bool
        A flag indicating if data retrieval is completed.
    """
    def __init__(self, symbol):
        """
        Initialize a new instance of the StockData class.

        Parameters
        ----------
        symbol : str
            The stock symbol of the company.
        """
        self.symbol = symbol
        self.urls = self._create_urls()
        self.company_data = self._create_dict_company()
        self.scrape_done = False
        self.retrieve_done = False


    def _create_urls(self):
        """
        Private method to construct the URLs for various financial statements.
        """
        ticker = self.symbol.lower()
        urls = {}

        # Quarterly Data
        urls['income_statement_quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/?p=quarterly"
        urls['balance_sheet_quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/balance-sheet/?p=quarterly"
        urls['cash_flow_statement_quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/cash-flow-statement/?p=quarterly"
        urls['ratios_quarterly'] = f"https://stockanalysis.com/stocks/{ticker}/financials/ratios/?p=quarterly"

        # Annual Data
        urls['income_statement_annual'] = f"https://stockanalysis.com/stocks/{ticker}/financials/"
        urls['balance_sheet_annual'] = f"https://stockanalysis.com/stocks/{ticker}/financials/balance-sheet/"
        urls['cash_flow_statement_annual'] = f"https://stockanalysis.com/stocks/{ticker}/financials/cash-flow-statement/"
        urls['ratios_annual'] = f"https://stockanalysis.com/stocks/{ticker}/financials/ratios/"
        
        return urls

    def _create_dict_company(self):
        """
        Private method to initialize a dictionary for storing all the company's data.
        """
        keys = ["income_statement", "balance_sheet", "cash_flow_statement", "ratios"]
        all_data_dict = {}

        for key in keys:
            all_data_dict[key] = {"annual": None, "quarterly": None}

        all_data_dict["stock_price"] = None
        all_data_dict["profile"] = None
        
        return all_data_dict


    def _process_key(self, key):
        """
        Private method to process the key of a URL.

        Parameters
        ----------
        key : str
            The key of a URL.
        """
        if "_quarterly" in key:
            frequency = "quarterly"
            processed_key = key.replace('_quarterly', '')    
        elif "_annual" in key:
            frequency = "annual"
            processed_key = key.replace('_annual', '')   
        else:
            frequency = None
            processed_key = key
        return processed_key, frequency

    def scrape_financial_statements(self):
        """
        Method to scrape financial statements for the company.
        """
        self.company_data = self._scrape_stock_analysis()
        self.scrape_done = True

    
    def _scrape_stock_analysis(self):
        """
        Private method to scrape the financial data of the company from stockanalysis.com.
        """

        for key in self.urls.keys():

            processed_key, frequency = self._process_key(key)

            try:
                page = requests.get(self.urls[key])
                page.raise_for_status()  # raises an HTTPError if the status is 4xx, 5xx

            except (requests.exceptions.HTTPError,
                    requests.exceptions.ConnectionError,
                    requests.exceptions.Timeout,
                    requests.exceptions.RequestException) as err:

                print (f"Error for {self.symbol}:", err)


                continue

            try:
                soup = BeautifulSoup(page.content, "html.parser")
                table = soup.find('table')

                # If data is not found continue to next element in the loop 
                if table is None:
                    continue
                # Else format data and save it 
                else: 
                    # Obtain colnames (which correspond to dates)
                    colnames = table.find_all('th')

                    # Cleaned column names (dates)
                    colnames = [date.text.strip() for date in colnames]

                    # Get the values of the different metrics
                    rows = table.find_all('tr')

                    # list to hold all table data
                    data = []

                    # iterate over each row
                    for row in rows:

                        # find all columns in the row
                        cols = row.find_all('td')

                        # get the text from the columns
                        cols = [col.text.strip() for col in cols]

                        # add the columns to the data array
                        data.append(cols)

                    # create a pandas dataframe from the data
                    df = pd.DataFrame(data)

                    # assign column names
                    df.columns = colnames

                    # rename Column name from Quarter Ended to Metrics
                    df = df.rename(columns={"Quarter Ended": "Metrics"})

                    # drop empty first row
                    df = df.drop(0)

                    # Save file in CSV (Should be run from pipeline folder)
                    df.to_csv(f"../data/raw/financial_statements/{processed_key}/{frequency}/{self.symbol}.csv", index = False)

                    # Save info in dictionary
                    self.company_data[processed_key][frequency] = df.to_dict()

            except AttributeError as e:
                print(f"Attribute Error for {self.symbol}:", e)
                continue

            except Exception as e:
                print(f"An unexpected error occurred for {self.symbol}:", e)

                continue

        return self.company_data


    
    
    def retrieve_profile_stock_price(self, start, end):
        """
        Method to retrieve stock price data and company profile from Yahoo Finance.

        Parameters
        ----------
        start : str
            The start date for the stock price data retrieval in the format 'YYYY-MM-DD'.
        end : str
            The end date for the stock price data retrieval in the format 'YYYY-MM-DD'.
        """
        try:
            # Retrieve data from Yahoo Finance
            sym = Ticker(self.symbol)
            
            # Obtain stock data
            stock_data = sym.history(start=start, end=end)
            
            # Get company profile 
            profile = sym.asset_profile[self.symbol]
            
            # Save CSV file 
            stock_data.reset_index().to_csv(f"../data/raw/stock_prices/{self.symbol}.csv", index = False)
            
            # Save company profile as JSON
            with open(f"../data/raw/company_profile/{self.symbol}.json", 'w') as f:
                json.dump(profile, f)

            self.company_data["stock_price"] = stock_data.reset_index().to_dict()
            self.company_data["profile"] = profile

        except Exception as e:
            print(f"An error occurred while retrieving data for {self.symbol}: {str(e)}")
            
        self.retrieve_done = True
        
        
    def save_to_json(self):
        """
        Method to save the scraped and retrieved company data in JSON format.
        """
        if self.scrape_done and self.retrieve_done:
            with open(f"../data/raw/json_data/{self.symbol}.json", 'w') as f:
                json.dump(self.company_data, f, default=date_handler)
        else:
            print("Scrape or retrieve_profile_stock_price methods have not been executed yet.")
