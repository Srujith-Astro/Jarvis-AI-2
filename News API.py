import requests

# Replace 'YOUR_API_KEY' with your actual NewsAPI API key
API_KEY = 'bcce7e06ddfc486cbc16d94b7d83f06b'
endpoint = 'https://newsapi.org/v2/top-headlines'

# Set the parameters for the request
params = {
    'apiKey': API_KEY,
    'country': 'ind',  # You can change this to the desired country code
}

# Make the request
response = requests.get(endpoint, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    articles = data['articles']
    for article in articles:
        print(article['title'])
else:
    print('Error:', response.status_code)
