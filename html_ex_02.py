# the names are in the same order in the HTML even though they shift around on the web page

# for this exercise we look for the link at position of 18 relative to the first name. we must repeat the process 7 times and print the last name that was retrieved

from urllib.request import urlopen
from bs4 import BeautifulSoup

n = 0
count = 0

#url = input('Enter url: ')
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
repeats = 4
#repeats  = int(input('Enter repeats count: '))
#position = int(input('Enter position: '))
position = 3

# 0, 1, 2, 3, 4
while n < repeats:
    page = urlopen(url).read()
    soup = BeautifulSoup(page, "html.parser")
    tags = soup('a')
    
    for tag in tags:
        count = count + 1
        if count == position:
            url = tag.get('href', None)
            print('Retrieving: ', url)
            count = 0
            break
#        Debugging:
#        else:
#            print("==================>>")
#            print(count)
#            print(position)
        
    n = n + 1 
    
    
    
    
    
    
    
    