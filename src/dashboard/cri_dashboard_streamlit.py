import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CRI data
FILE_PATH = "data/final/cri_final.csv"
df = pd.read_csv(FILE_PATH)

# Streamlit Configuration
st.set_page_config(page_title="Currency Risk Index Dashboard", layout="wide")

# Title
st.title("Currency Risk Index (CRI) Dashboard")

# CRI Trend Visualization
st.subheader("Currency Risk Index (CRI) Trends Over Time")
fig = px.line(
    df,
    x="year",
    y="CRI",
    title="Currency Risk Index (CRI) Trends",
    markers=True,
    labels={"year": "Year", "CRI": "Currency Risk Index (CRI)"},
)
fig.update_layout(
    template="plotly_white",
    hovermode="x unified",
    title_font_size=20,
    xaxis_title_font_size=14,
    yaxis_title_font_size=14,
)
st.plotly_chart(fig, use_container_width=True)

# Yearly CRI Details
st.subheader("Yearly CRI Details")
selected_year = st.selectbox("Select a Year:", df["year"])
year_data = df[df["year"] == selected_year]
st.write(f"Details for the year {selected_year}:")
st.dataframe(year_data)

# Metric Contribution to CRI
st.subheader("Metric Contribution to CRI")
if not year_data.empty:
    metric_cols = ["close_volatility", "close_returns", "GDP_value_yoy"]
    metric_data = year_data[metric_cols].transpose()
    metric_data.columns = ["Value"]
    metric_data["Metric"] = metric_data.index
    fig_contribution = px.bar(
        metric_data,
        x="Metric",
        y="Value",
        title=f"Metric Contribution to CRI for {selected_year}",
        labels={"Value": "Metric Value", "Metric": "Metric"},
    )
    st.plotly_chart(fig_contribution, use_container_width=True)
