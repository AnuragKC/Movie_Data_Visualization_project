import requests
import pandas as pd

API_KEY = 'INPUT UR API KEY HERE, CAN GET IT FROM TMDB'
DISCOVER_URL = 'https://api.themoviedb.org/3/discover/movie'
MOVIE_URL = 'https://api.themoviedb.org/3/movie/'


def fetch_movie_details(movie_id):
    params = {
        'api_key': API_KEY,
    }
    response = requests.get(f"{MOVIE_URL}{movie_id}", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} for movie ID {movie_id}")
        return None


def fetch_movies(page=1):
    params = {
        'api_key': API_KEY,
        'sort_by': 'revenue.desc',
        'page': page,
    }
    response = requests.get(DISCOVER_URL, params=params)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Error: {response.status_code}")
        return None


def main():
    movies = []
    for page in range(1, 6):  # Fetch first 5 pages
        data = fetch_movies(page)
        if data:
            for movie in data:
                movie_id = movie['id']
                movie_details = fetch_movie_details(movie_id)
                if movie_details:
                    movie['revenue'] = movie_details.get('revenue', 0)
                    movies.append(movie)

    # Saving the data to a CSV
    df = pd.DataFrame(movies)
    df.to_csv('movies.csv', index=False)
    print("Movies data with revenue saved to movies.csv")


if __name__ == "__main__":
    main()
