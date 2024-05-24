from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

quotes = soup.find_all("span",  {"class": "text"})
for quote in quotes:
    print(quote.text)
