##This script fetches daily exchange rate data for the specified USD pairs (USD/EUR, USD/JPY, USD/GBP) using Alpha Vantage.

import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

# Directory for saving raw data
RAW_DATA_DIR = "data/raw/"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

def fetch_exchange_rate_data(from_currency, to_currency, output_file):
    """
    Fetch daily exchange rate data from Alpha Vantage and filter for the 2004–2024 range.

    Args:
        from_currency (str): Base currency (e.g., "USD").
        to_currency (str): Target currency (e.g., "EUR").
        output_file (str): Filepath to save the raw data as CSV.

    Returns:
        pd.DataFrame: DataFrame containing the filtered exchange rate data.
    """
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "FX_DAILY",
        "from_symbol": from_currency,
        "to_symbol": to_currency,
        "apikey": ALPHA_VANTAGE_API_KEY,
        "outputsize": "full",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "Time Series FX (Daily)" in data:
            df = pd.DataFrame.from_dict(data["Time Series FX (Daily)"], orient="index")
            df = df.rename(
                columns={
                    "1. open": "open",
                    "2. high": "high",
                    "3. low": "low",
                    "4. close": "close",
                }
            )
            df.index = pd.to_datetime(df.index)  # Convert index to datetime
            df = df.sort_index()  # Ensure data is sorted by date
            df = df[(df.index >= "2004-01-01") & (df.index <= "2024-12-31")]  # Filter by date range
            df.to_csv(output_file)
            print(f"Saved exchange rate data for {from_currency}/{to_currency} to {output_file}")
            return df
    else:
        print(f"Failed to fetch exchange rate data for {from_currency}/{to_currency}: {response.status_code}")
        return None

if __name__ == "__main__":
    # Fetch data for USD pairs
    pairs = [("USD", "EUR"), ("USD", "JPY"), ("USD", "GBP")]
    for from_currency, to_currency in pairs:
        output_file = f"{RAW_DATA_DIR}{from_currency}_{to_currency}.csv"
        fetch_exchange_rate_data(from_currency, to_currency, output_file)
