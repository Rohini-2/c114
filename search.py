import pandas as pd
import plotly.express as px

df = pd.read_csv("velocity.csv")

temperature_list = df["Velocity"].tolist()
melted_list = df["Escaped"].tolist()

fig = px.scatter(x=temperature_list, y=melted_list)
fig.show()