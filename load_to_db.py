import pandas as pd
from sqlalchemy import create_engine, BigInteger
from sqlalchemy.types import Integer, Float, Date


engine = create_engine('postgresql://username:password@localhost:5432/movies_db')


def load_to_db():
    try:
        # Read data from CSV
        df = pd.read_csv('movies.csv')

        # Select relevant columns
        df = df[['title', 'revenue', 'release_date', 'genre_ids', 'vote_average']]

        # Load data into the database
        df.to_sql('movies', engine, if_exists='replace', index=False, dtype={
            'revenue': BigInteger(),
            'release_date': Date(),
            'vote_average': Float(),
        })
        print("Data loaded to database!")

    except Exception as e:
        print(f"Error loading data: {e}")


if __name__ == "__main__":
    load_to_db()
