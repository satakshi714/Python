import requests
from bs4 import BeautifulSoup

url="https://books.toscrape.com/"

r=requests.get(url)
htmlcont=r.content
# print("htmlcont")

BeautifulSoup(htmlcont,"html.parser")
print(soup.prettify)