import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load your dataset
data = pd.read_csv("Toddler Autism dataset July 2018.csv")


# Initialize the Dash app
app = dash.Dash(__name__)

# Create a list of dropdown options for columns
dropdown_options = [{'label': col, 'value': col} for col in data.columns]

# Dash app layout
app.layout = html.Div([
    html.H1("Dataset Dashboard"),
    dcc.Dropdown(
        id='column-dropdown',
        options=dropdown_options,
        value=dropdown_options[0]['value']  # Default value
    ),
    dcc.Graph(id='count-plot')
])

# Callback to update graph based on dropdown selection
@app.callback(
    Output('count-plot', 'figure'),
    [Input('column-dropdown', 'value')]
)
def update_graph(selected_column):
    fig = px.histogram(data, x=selected_column, title=f"Count Plot of {selected_column}")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
