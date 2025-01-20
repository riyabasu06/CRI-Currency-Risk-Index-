import os
import pandas as pd

# Directory paths
RESAMPLED_DATA_DIR = "data/resampled/"
PROCESSED_DATA_DIR = "data/processed/"
MERGED_DATA_DIR = "data/merged/"
os.makedirs(MERGED_DATA_DIR, exist_ok=True)

def merge_datasets(world_bank_file, alpha_vantage_file, output_file):
    """
    Merge World Bank yearly data with Alpha Vantage yearly data.

    Args:
        world_bank_file (str): Path to the processed World Bank file.
        alpha_vantage_file (str): Path to the resampled Alpha Vantage file.
        output_file (str): Path to save the merged dataset.

    Returns:
        pd.DataFrame: Merged dataset.
    """
    # Load the datasets
    wb_data = pd.read_csv(world_bank_file)
    av_data = pd.read_csv(alpha_vantage_file)

    # Merge on the 'year' column
    merged_data = pd.merge(wb_data, av_data, on="year", how="inner")

    # Save the merged dataset
    merged_data.to_csv(output_file, index=False)
    print(f"Merged data saved to {output_file}")
    return merged_data

if __name__ == "__main__":
    # Merge GDP growth with USD/EUR data
    merge_datasets(
        f"{PROCESSED_DATA_DIR}gdp_growth_rate_processed.csv",
        f"{RESAMPLED_DATA_DIR}USD_EUR_yearly.csv",
        f"{MERGED_DATA_DIR}gdp_growth_usd_eur.csv"
    )
