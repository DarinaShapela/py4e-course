from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)
xml = urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = ET.fromstring(xml)
users = tree.findall('comments/comment')
print('Users count: ', len(users))

values = list()
for number in users:
    num = number.find('count').text
    values.append(int(num))

print(sum(values))