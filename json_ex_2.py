import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

location = input('Enter address: ')
url = serviceurl + urllib.parse.urlencode({'address': location, 'key' : 42})
print('Retrieving', url)
url_handle = urllib.request.urlopen(url)
data = url_handle.read().decode()
print('Retrieved', len(data), 'characters')

js_info = json.loads(data)
place_id = js_info['results'][0]['place_id']
print('The Place ID is: ', place_id)