from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter url: ')
page = urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

# Retrieve all of the span tags
tags = soup('span')

# sum up values of span tags
values = list()

for tag in tags:
    values.append(int(tag.string))

print(sum(values))
    
