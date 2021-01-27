import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Main_Page')

type(result)