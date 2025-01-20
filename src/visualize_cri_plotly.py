import pandas as pd
import plotly.express as px
from plotly.offline import plot

# Load the CRI data
FILE_PATH = "data/final/cri_final.csv"
df = pd.read_csv(FILE_PATH)

# Create the CRI trend plot
def plot_cri_trends(data, output_html=None):
    """
    Plot interactive CRI trends using Plotly and optionally save as an HTML file.

    Args:
        data (pd.DataFrame): DataFrame containing 'year' and 'CRI' columns.
        output_html (str): File path to save the HTML file. If None, the file is not saved.
    """
    fig = px.line(
        data, 
        x="year", 
        y="CRI", 
        title="Currency Risk Index (CRI) Trends Over Time",
        labels={"year": "Year", "CRI": "Currency Risk Index (CRI)"},
        markers=True
    )
    fig.update_traces(line_color="blue")
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        template="plotly_white",
        hovermode="x unified",
    )
    fig.add_hline(
        y=0, 
        line_dash="dash", 
        line_color="gray", 
        annotation_text="Neutral CRI", 
        annotation_position="top left"
    )

    # Save the figure as an HTML file (if output_html is provided)
    if output_html:
        plot(fig, filename=output_html)
        print(f"Plot saved as: {output_html}")

# Plot CRI trends and save to an HTML file
output_html_path = "cri_trends.html"
plot_cri_trends(df, output_html=output_html_path)
