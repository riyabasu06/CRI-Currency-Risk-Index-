##Calculate Derived Metrics:
#1. Exchange Rate Volatility:
#       Calculate rolling standard deviation (e.g., over 30 days).
#2. Exchange Rate Returns:
#       Compute daily or monthly percentage changes.
#3. Year-over-Year Changes:
#       For macroeconomic indicators like debt-to-GDP ratio, calculate annual changes.

def calculate_volatility(data, column, window):
    """
    Calculate rolling volatility (standard deviation).
    """
    data[f"{column}_volatility"] = data[column].rolling(window).std()
    return data

def calculate_returns(data, column):
    """
    Calculate percentage returns for a given column.
    """
    data[f"{column}_returns"] = data[column].pct_change() * 100
    return data

def calculate_yoy_change(data, column):
    """
    Calculate year-over-year changes.
    """
    data[f"{column}_yoy_change"] = data[column].diff(1)
    return data
