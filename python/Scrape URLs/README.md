## URL scraper

Do you want to scrape all the links from a website?
Well it's easy with Python.

Steps:
1. DOwnload webpage data i.e. HTML.
2. Create beautifulsoup object and parse webpage data.
3. Use soup methods **findAll** to find all the links by the tag.
4. The result will be stored in a list.

## Code

```
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
```

## Understanding the Code

```
url = input("Enter a website URL:")

req = Request(url)
html_page = urlopen(req)
```
A URL will be taken from the user. And the webpage data will be downloaded (HTML tags).

```
soup = BeautifulSoup(html_page, "lxml")
```
This line loads it into a BeautifulSoup object.


```
links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))
```
This line will extract all the links, since we know that the a tag is used to store the links in HTML, so it'll search for those.

```
print(links)
```

And this will print all the links from a particular website.
