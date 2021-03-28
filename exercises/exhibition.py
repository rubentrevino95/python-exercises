import requests
from bs4 import BeautifulSoup

result = requests.get('https://en.wikipedia.org/wiki/Main_Page')

print(type(result))
# print(result.text)