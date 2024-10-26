from urllib.request import urlopen

from bs4 import BeautifulSoup

n = 0
count = 0

url = input("Enter url: ")
repeats = int(input("Enter repeats count: "))
position = int(input("Enter position: "))


while n < repeats:
    page = urlopen(url).read()
    soup = BeautifulSoup(page, "html.parser")
    tags = soup("a")

    for tag in tags:
        count = count + 1
        if count == position:
            url = tag.get("href", None)
            print("Retrieving: ", url)
            count = 0
            break
    n = n + 1
