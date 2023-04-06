from bs4 import BeautifulSoup
import requests
import pandas as pd

# Request page source from URL
URL = "https://www.imdb.com/chart/top/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Scrape Movie Names
scraped_movies = soup.find_all('td', class_='titleColumn')
scraped_movies

# Parse Movie Names
movies = []
for movie in scraped_movies:
    movie = movie.get_text().replace('\n', "").strip(" ")
    movies.append(movie)
movies

# Scrape Ratings for Movies
scraped_ratings = soup.find_all('td', class_='ratingColumn imdbRating')
scraped_ratings

# Parse Ratings for Movies
ratings = []
for rating in scraped_ratings:
    rating = rating.get_text().replace('\n','')
    ratings.append(rating)
ratings

# Store the Scraped Data
data = pd.DataFrame()
data['Movie Names'] = movies
data['Ratings'] = ratings
data.head()

data.to_csv('IMDB Top Movies.csv', index=False)
