import requests
import json

query = input("What type of news are you interested in? ")

api_key = "49c0a61944644e2d9ef34c1b3b5129d4"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-08-28&sortBy=publishedAt&apiKey={api_key}"

r = requests.get(url)

news = json.loads(r.text)

# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------")
