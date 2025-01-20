## Clean and standardize(Z-score) the yearly World Bank data.

import os
import pandas as pd

# Directory paths
RAW_DATA_DIR = "data/raw/"
PROCESSED_DATA_DIR = "data/processed/"
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

def standardize_column(df, column):
    """
    Standardize a column using Z-Score scaling.

    Args:
        df (pd.DataFrame): DataFrame containing the column to standardize.
        column (str): Column to standardize.

    Returns:
        pd.DataFrame: DataFrame with a new standardized column.
    """
    mean = df[column].mean()
    std = df[column].std()
    df[f"{column}_zscore"] = (df[column] - mean) / std
    return df

def preprocess_world_bank(file_path, output_file):
    """
    Preprocess World Bank yearly data: handle missing values, standardize.

    Args:
        file_path (str): Path to the input file.
        output_file (str): Path to save the processed file.

    Returns:
        None
    """
    # Load the raw data
    df = pd.read_csv(file_path)

    # Ensure the expected column exists
    if "value" not in df.columns:
        raise KeyError(f"Column 'value' not found in {file_path}. Available columns: {df.columns}")

    # Handle missing values using forward fill
    df = df.ffill()

    # Standardize the 'value' column
    df = standardize_column(df, "value")

    # Save the processed data
    df.to_csv(output_file, index=False)
    print(f"Processed World Bank data saved to {output_file}")

if __name__ == "__main__":
    # List of World Bank indicator files to preprocess
    indicators = ["inflation_rate", "gdp_growth_rate", "unemployment_rate", "debt_to_gdp_ratio"]
    for indicator in indicators:
        input_file = f"{RAW_DATA_DIR}{indicator}.csv"
        output_file = f"{PROCESSED_DATA_DIR}{indicator}_processed.csv"
        preprocess_world_bank(input_file, output_file)
