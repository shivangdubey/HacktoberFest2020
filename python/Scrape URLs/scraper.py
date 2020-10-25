from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

url = input("Enter a website URL:")

req = Request(url)
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)