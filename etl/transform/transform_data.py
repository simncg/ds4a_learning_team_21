# %%
# Import libraries to be used 
import os
import sys
import pandas as pd 
import json 
import datetime
import numpy as np

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data")


class FinStmtRatioCleaner:
    """
    A class used to clean and transform financials statements and financial ratios data.

    Attributes
    ----------
    data : pandas.DataFrame
        the financial ratio data to be cleaned and transformed
    """
    def __init__(self, data: pd.DataFrame, period:str):
        """
        Constructs the FinancialRatioDataCleaner class with the provided financial ratio data.

        Parameters
        ----------
        data : pandas.DataFrame
            The financial ratio data to be cleaned and transformed.
        """
        if period not in ["annual", "quarterly"]:
            raise ValueError("Period must be either 'annual' or 'quarterly'")
        self.data = data
        self.period = period
        

    def __transpose_data(self):
        """
        Transposes the data to have dates as an index.
        """
        self.data = self.data.transpose()
        self.data.columns = self.data.iloc[0]
        self.data = self.data[1:]

    def __clean_names(self, name: str) -> str:
        """
        Cleans the column names by replacing special characters with '_'.

        Parameters
        ----------
        name : str
            The name to be cleaned.

        Returns
        -------
        str
            The cleaned name.
        """
        name = name.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("_/_", "_or_").replace("&", "and").replace("__", "_").replace(",", "").replace("-", "_").replace("'", "").replace("/", "_over_")
        return name
    
    def __clean_variable_numbers(self, column: pd.Series) -> pd.Series:
        """
        Cleans the data in the columns by replacing certain characters and converting to numeric.

        Parameters
        ----------
        column : pandas.Series
            The column data to be cleaned.

        Returns
        -------
        pandas.Series
            The cleaned column data.
        """
        column = column.str.replace(",", "")
        column = column.str.replace("%", "")
        column = column.str.replace("-", "")
        return pd.to_numeric(column, errors='coerce')
        
    def clean_data(self):
        """
        Cleans and transforms the financial ratio data. This involves transposing the data, normalizing column names,
        resetting the index, renaming the index column, removing specific observations in the date column, cleaning all
        columns to numeric except the date column, and formatting the date column.
        """

        if self.data.empty:
            return pd.DataFrame() # return an empty DataFrame

        self.__transpose_data()
        self.data.columns = [self.__clean_names(name) for name in self.data.columns]
        self.data = self.data.reset_index()
        self.data = self.data.rename(columns={"index": "date"})
        # If it is quarterly data it will remove the extra row indicating the information what we can gain acces if we pay
        self.data = self.data[~self.data['date'].str.contains('Quarter')]
        self.data = self.data[~self.data['date'].str.contains('Current')]
        columns_to_clean = [col for col in self.data.columns if col != 'date']
        self.data[columns_to_clean] = self.data[columns_to_clean].apply(self.__clean_variable_numbers)
        # If it is annual data in the last row we will have something like 2012-1994 (and empty values because these need to be paid, so we will drop this row)
        if self.period == "annual":
            self.data = self.data.iloc[:-1]
            # Set date format to data
            self.data["date"] = pd.to_datetime(self.data["date"], format = "%Y")
        elif self.period == "quarterly":
            self.data["date"] = pd.to_datetime(self.data["date"], format = "%Y-%m-%d")


class ProfileCleaner:
    """
    A class used to clean and transform financials statements and financial ratios data.

    Attributes
    ----------
    data : pandas.DataFrame
        the financial ratio data to be cleaned and transformed
    """
    def __init__(self, profile_dict: dict):
        """
        Constructs the FinancialRatioDataCleaner class with the provided financial ratio data.

        Parameters
        ----------
        profile_dict : dict
            The financial ratio data to be cleaned and transformed.
        """
        self.profile_dict = profile_dict
        self.profile_data = None
    
    def clean_data(self):
        selected_keys = ["sector","industry", "website", "longBusinessSummary", 
                         "address1", "city", "state", "zip", "country", 
                         "latitude", "longitude", "fullTimeEmployees"]
        
        # Use dictionary comprehension to select the keys
        # If the key is not found in the dictionary, np.nan will be used as the value
        self.profile_data = pd.DataFrame([{key: self.profile_dict.get(key, np.nan) for key in selected_keys}])


class StockDataCleaner():
    """
    A class used to clean and transform financials statements and financial ratios data.

    Attributes
    ----------
    data : pandas.DataFrame
        the financial ratio data to be cleaned and transformed
    """
    def __init__(self, stock_data_dict: dict):
        """
        Constructs the FinancialRatioDataCleaner class with the provided financial ratio data.

        Parameters
        ----------
        profile_dict : dict
            The financial ratio data to be cleaned and transformed.
        """
        self.stock_data_dict = stock_data_dict
        self.stock_data = pd.DataFrame()  # set default value for stock_data


    def clean_data(self):
        if pd.DataFrame(self.stock_data_dict).empty:
            print("The stock data frame is empty.")

        self.stock_data = pd.DataFrame(self.stock_data_dict)
        self.stock_data["date"] = pd.to_datetime(self.stock_data["date"])

    

        


class DataCleaner:
    """
    A class to handle financial data extraction and cleaning from JSON files.

    Attributes
    ----------
    symbol : str
        Symbol of the financial entity.
    data : dict
        Dictionary to store the cleaned data frames.
    """
    
    def __init__(self, symbol: str):
        """
        Constructs the FinancialDataHandler class with the provided symbol.

        Parameters
        ----------
        symbol : str
            Symbol of the financial entity.
        """
        self.symbol = symbol
        self.data = {}

    def load_and_clean_data(self):
        """
        Loads the financial data from a JSON file and applies the cleaning process for each data frame.
        """
        with open(os.path.join(DATA_PATH, "raw", "json_data", f"{self.symbol}.json"), 'r') as f:
            all_data = json.load(f)
        
        for key1 in all_data:
            if key1 not in ["profile", "stock_price"]:
                for key2 in all_data[key1]:
                    cleaner = FinStmtRatioCleaner(pd.DataFrame(all_data[key1][key2]), key2)
                    cleaner.clean_data()
                    self.data[f'{key1}_{key2}'] = cleaner.data
                    self.data[f'{key1}_{key2}'].insert(loc=0, column='symbol', value=self.symbol)

            elif key1 == "profile":
                cleaner = ProfileCleaner(all_data["profile"])
                cleaner.clean_data()
                self.data["profile"] = cleaner.profile_data
                self.data['profile'].insert(loc=0, column='symbol', value=self.symbol)

            elif key1 == "stock_price":
                cleaner = StockDataCleaner(all_data["stock_price"])
                cleaner.clean_data()
                self.data["stock_price"] = cleaner.stock_data



class FinancialDataTransformer:
    """
    A class to handle financial data extraction, cleaning and joining from multiple JSON files.

    Attributes
    ----------
    symbols : list
        List of symbols of the financial entities.
    data : dict
        Dictionary to store the cleaned and joined data frames.
    """
    def __init__(self, symbols: list):
        """
        Constructs the FinancialDataProcessor class with the provided symbols.

        Parameters
        ----------
        symbols : list
            List of symbols of the financial entities.
        """
        self.symbols = symbols
        self.data = {}

    def transform(self):
        """
        Loads and cleans the financial data for all symbols from the JSON files.
        Joins the data frames of the same type from all symbols.
        """

        for symbol in self.symbols:
            try:
                transformer = DataCleaner(symbol)
                transformer.load_and_clean_data()

                for key, df in transformer.data.items():
                    if key not in self.data:
                        self.data[key] = df
                    else:
                        self.data[key] = pd.concat([self.data[key], df])

            except Exception as e:
                print(f"Skipped symbol {symbol} due to error: {e}")

        # Reset the index for each DataFrame
        for key in self.data:
            self.data[key].reset_index(drop=True, inplace=True)

    def save_to_csv(self):
        """
        Saves the processed data frames to CSV files.
        Each CSV file is named after its corresponding key in the data dictionary.
        The CSV files are saved in the "processed" sub-directory of the DATA_PATH directory.
        """

        os.makedirs(os.path.join(DATA_PATH, "processed"), exist_ok=True)

        for key, df in self.data.items():
            df.to_csv(os.path.join(DATA_PATH, "processed", f"{key}.csv"), index=False)


