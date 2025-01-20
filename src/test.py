import plotly.express as px
import pandas as pd

df = pd.DataFrame({"x": [1, 2, 3], "y": [3, 6, 9]})
fig = px.scatter(df, x="x", y="y", title="Test Plot")
fig.show()
