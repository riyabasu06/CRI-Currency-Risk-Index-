import pandas as pd
import os

# Directory paths
METRICS_DATA_DIR = "data/metrics/"
FINAL_DATA_DIR = "data/final/"
os.makedirs(FINAL_DATA_DIR, exist_ok=True)

def calculate_cri(data, weights):
    """
    Calculate the Currency Risk Index (CRI) by combining weighted indicators.

    Args:
        data (pd.DataFrame): DataFrame containing metrics.
        weights (dict): Dictionary of weights for each metric.

    Returns:
        pd.DataFrame: DataFrame with CRI score added.
    """
    # Ensure all metrics exist in the dataset
    missing_columns = [col for col in weights if col not in data.columns]
    if missing_columns:
        raise KeyError(f"Missing columns in dataset: {missing_columns}")

    # Calculate the weighted sum for CRI
    data["CRI"] = sum(data[metric] * weight for metric, weight in weights.items())
    return data

if __name__ == "__main__":
    # Define weights for each metric
    weights = {
        "close_volatility": 0.4,  # Exchange rate volatility
        "close_returns": 0.3,    # Exchange rate returns
        "GDP_value_yoy": 0.3,    # GDP YoY changes
    }

    # Load the metrics dataset
    metrics_file = f"{METRICS_DATA_DIR}gdp_growth_usd_eur_with_metrics.csv"
    df = pd.read_csv(metrics_file)

    # Calculate CRI
    cri_df = calculate_cri(df, weights)

    # Save the final dataset with CRI
    output_file = f"{FINAL_DATA_DIR}cri_final.csv"
    cri_df.to_csv(output_file, index=False)
    print(f"CRI calculation complete. Saved to {output_file}")
