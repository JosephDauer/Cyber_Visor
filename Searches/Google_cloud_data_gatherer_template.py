#google cloud data gatherer
import requests

#API and SEARCH ENGINE ID
API_KEY = ''
SEARCH_ENGINE_ID = ''

#URL for Google Custom Search API
query = ''
url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}'

response = requests.get(url)

#Define response parameters
if response.status_code == 200:
    data = response.json()
    for item in data.get('items', []):
        title = item.get('title')
        link = item.get('link')
        snippet = item.get('snippet')
        print(f'Title: {title}')
        print(f'Link: {link}')
        print(f'Snippet: {snippet}')

else:
    print(f'Error: {response.status_code}')