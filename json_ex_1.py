import urllib.request, urllib.parse, urllib.error
import json
count = 0
values = list()

url = input('Enter url: ')
print('Retrieving:' , url)
url_handle = urllib.request.urlopen(url)

data = url_handle.read()
print('Retrieved', len(data), 'characters')

js_info = json.loads(data)
comments = js_info['comments']
for user in comments:
    count = count + 1
    values.append(user['count'])

print('Users count: ', count)
print('Sum:' , sum(values))