from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the CRI data
FILE_PATH = "data/final/cri_final.csv"
df = pd.read_csv(FILE_PATH)

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Currency Risk Index (CRI) Dashboard", style={"textAlign": "center"}),

    # CRI Trend Plot
    dcc.Graph(id="cri-trend-plot"),
    html.Label("Select a Year:"),
    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": year, "value": year} for year in df["year"]],
        value=df["year"].min(),
        clearable=False,
    ),

    # Yearly Metric Contribution Plot
    dcc.Graph(id="metric-contribution-plot"),
])

# Callbacks for interactivity
@app.callback(
    [Output("cri-trend-plot", "figure"), Output("metric-contribution-plot", "figure")],
    [Input("year-dropdown", "value")]
)
def update_dashboard(selected_year):
    # CRI Trends
    cri_fig = px.line(
        df,
        x="year",
        y="CRI",
        title="Currency Risk Index (CRI) Trends",
        markers=True,
    )
    cri_fig.update_layout(template="plotly_white", hovermode="x unified")

    # Metric Contribution
    year_data = df[df["year"] == selected_year]
    metric_cols = ["close_volatility", "close_returns", "GDP_value_yoy"]
    metric_data = year_data[metric_cols].transpose()
    metric_data.columns = ["Value"]
    metric_data["Metric"] = metric_data.index
    metric_fig = px.bar(
        metric_data,
        x="Metric",
        y="Value",
        title=f"Metric Contribution to CRI for {selected_year}",
    )
    return cri_fig, metric_fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
