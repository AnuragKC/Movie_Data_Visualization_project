import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('aggregated_data.csv')


if df['year'].isnull().any():
    print("Missing values found in 'year' column. Handling missing values...")

    
    df.dropna(subset=['year'], inplace=True)

# Ensure that the 'year' column is an integer after handling missing values
df['year'] = df['year'].astype(int)


app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("Movie Revenue and Ratings Dashboard", style={'text-align': 'center'}),

    # Chart for Total Revenue by Year
    html.Div([
        dcc.Graph(
            id='revenue-chart',
            figure=px.line(df, x='year', y='total_revenue', title='Total Revenue by Year')
        )
    ], style={'padding': '20px'}),

    # Chart for Average Rating by Year
    html.Div([
        dcc.Graph(
            id='rating-chart',
            figure=px.line(df, x='year', y='avg_rating', title='Average Rating by Year')
        )
    ], style={'padding': '20px'})
])


if __name__ == '__main__':
    app.run_server(debug=True)
