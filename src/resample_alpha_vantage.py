## Resample Alpha Vantage Data into into yearly averages

import os
import pandas as pd

# Directory paths
RAW_DATA_DIR = "data/raw/"
RESAMPLED_DATA_DIR = "data/resampled/"
os.makedirs(RESAMPLED_DATA_DIR, exist_ok=True)

def resample_to_yearly(file_path, output_file):
    """
    Resample daily Alpha Vantage data to yearly averages and save to a new file.

    Args:
        file_path (str): Path to the raw Alpha Vantage daily data.
        output_file (str): Path to save the resampled yearly data.
    """
    # Load daily data
    df = pd.read_csv(file_path, parse_dates=["timestamp"], index_col="timestamp", dayfirst=True)
    
    # Fill missing days with forward-fill method (optional)
    df = df.resample("D").ffill()

    # Resample to yearly frequency using the mean for numeric columns
    yearly_data = df.resample("YE").mean()

    # Reset the index and extract only the year for the index
    yearly_data.index = yearly_data.index.year
    yearly_data.reset_index(inplace=True)
    yearly_data.rename(columns={"index": "year"}, inplace=True)

    # Save the resampled data
    yearly_data.to_csv(output_file, index=False)
    print(f"Resampled data saved to {output_file}")

if __name__ == "__main__":
    # List of raw files to process
    files = [
        ("USD_EUR", f"{RAW_DATA_DIR}USD_EUR.csv"),
        ("USD_JPY", f"{RAW_DATA_DIR}USD_JPY.csv"),
        ("USD_GBP", f"{RAW_DATA_DIR}USD_GBP.csv"),
    ]
    
    # Process each file and save the resampled data
    for name, file_path in files:
        output_file = f"{RESAMPLED_DATA_DIR}{name}_yearly.csv"
        resample_to_yearly(file_path, output_file)
