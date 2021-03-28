import requests
from bs4 import BeautifulSoup

result = requests.get('https://en.wikipedia.org/wiki/Main_Page')

type(result)
print(result.text)

soup = BeautifulSoup(src, 'lxml')

for link in links:
    # if "link" in link.text:
    #     print(link)
    # printing out attribute content
    print(link.attrs['href'])

print(soup.select('title')[0].getText())

site_paragraphs = soup.select('p')

print(site_paragraphs[0].getText())
