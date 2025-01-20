## This script fetches macroeconomic data for the US using the World Bank API for the specified indicators.

import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Directory for saving raw data
RAW_DATA_DIR = "data/raw/"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

def fetch_world_bank_data(indicator, start_year, end_year, country="US", output_file=None):
    """
    Fetch annual macroeconomic data from the World Bank API for the specified indicator and range.

    Args:
        indicator (str): Indicator code (e.g., "FP.CPI.TOTL.ZG" for inflation rate).
        start_year (int): Start year for the data (e.g., 2004).
        end_year (int): End year for the data (e.g., 2024).
        country (str): Country code (default is "US").
        output_file (str): Filepath to save the data as CSV (optional).

    Returns:
        pd.DataFrame: DataFrame containing the indicator data.
    """
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&date={start_year}:{end_year}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 1:  # Check if data exists
            df = pd.DataFrame(data[1])
            df = df[["date", "value"]]  # Keep relevant columns
            df = df.rename(columns={"date": "year", "value": indicator})
            df["year"] = pd.to_numeric(df["year"])  # Ensure year is numeric
            if output_file:
                df.to_csv(output_file, index=False)
                print(f"Saved World Bank data for {indicator} to {output_file}")
            return df
    else:
        print(f"Failed to fetch World Bank data for {indicator}: {response.status_code}")
        return None

if __name__ == "__main__":
    # Indicators and their World Bank codes
    indicators = {
        "inflation_rate": "FP.CPI.TOTL.ZG",
        "gdp_growth_rate": "NY.GDP.MKTP.KD.ZG",
        "unemployment_rate": "SL.UEM.TOTL.ZS",
        "debt_to_gdp_ratio": "GC.DOD.TOTL.GD.ZS",
    }

    for name, code in indicators.items():
        output_file = f"{RAW_DATA_DIR}{name}.csv"
        fetch_world_bank_data(code, 2004, 2024, "US", output_file)
