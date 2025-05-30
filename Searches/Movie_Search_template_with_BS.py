# Movie Search template with BeautifulSoup
from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/chart/top/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.find_all('td', class_='titleColumn')

# Extracting all ratings
data = soup.find_all('td', class_='ratingColumn imdbRating')
ratings = []
for rating in data:
    ratings.append(rating.text.strip()) 

# Printing the ratings
for i in range(len(movies)):
    print(f"Movie: {movies[i].a.text.strip()}")
    print(f"Rating: {ratings[i]}")
    print("-" * 20)

else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
