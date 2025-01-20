import pandas as pd
import os

# Directory paths
MERGED_DATA_DIR = "data/merged/"
METRICS_DATA_DIR = "data/metrics/"
os.makedirs(METRICS_DATA_DIR, exist_ok=True)

def calculate_derived_metrics(df, column, metric_type, window=3):
    """
    Calculate derived metrics (volatility, returns, or YoY change).

    Args:
        df (pd.DataFrame): DataFrame containing the column.
        column (str): Column to calculate metrics for.
        metric_type (str): Type of metric ('volatility', 'returns', 'yoy').
        window (int): Rolling window size (default is 3 for volatility).

    Returns:
        pd.DataFrame: DataFrame with the new metric column added.
    """
    if metric_type == "volatility":
        df[f"{column}_volatility"] = df[column].rolling(window).std()
    elif metric_type == "returns":
        df[f"{column}_returns"] = df[column].pct_change() * 100
    elif metric_type == "yoy":
        df[f"{column}_yoy"] = df[column].diff()
    return df

if __name__ == "__main__":
    # Load the merged dataset
    merged_file = f"{MERGED_DATA_DIR}gdp_growth_usd_eur.csv"
    df = pd.read_csv(merged_file)

    # Calculate volatility for exchange rates
    df = calculate_derived_metrics(df, "close", "volatility", window=3)

    # Calculate returns for exchange rates
    df = calculate_derived_metrics(df, "close", "returns")

    # Calculate YoY changes for exchange rates
    df = calculate_derived_metrics(df, "close", "yoy")

    # Calculate YoY changes for GDP values
    df = calculate_derived_metrics(df, "GDP_value", "yoy")

    # Save the dataset with metrics
    output_file = f"{METRICS_DATA_DIR}gdp_growth_usd_eur_with_metrics.csv"
    df.to_csv(output_file, index=False)
    print(f"Metrics calculated and saved to {output_file}")
