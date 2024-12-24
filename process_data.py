from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://username:password@localhost:5432/movies_db')

def get_aggregated_data():
    # SQL query to aggregate data by year
    query = """
    SELECT
        EXTRACT(YEAR FROM release_date) AS year,
        SUM(revenue) AS total_revenue,
        AVG(vote_average) AS avg_rating
    FROM movies
    GROUP BY year
    ORDER BY year;
    """
    # Fetch the aggregated data into a pandas DataFrame
    return pd.read_sql(query, engine)

if __name__ == "__main__":
    # Get aggregated data
    df = get_aggregated_data()

    # Ensure the data is saved to CSV
    df.to_csv('aggregated_data.csv', index=False)

    print("Aggregated data saved to 'aggregated_data.csv'!")
