import requests

query = input("what type of news are you intrested in today?")
api = "889b53ddf38c47b2ae214d91e362aa38"

url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print( index + 1, article["title"], article["url"])
    print("\n*****************************************\n")
