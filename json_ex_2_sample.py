# Calling a JSON API

# program should prompt for a location, contact a web service and retrieve JSON for the web service 
# parse that data, and retrieve the first place_id from the JSON. 
# a place ID is a textual identifier that uniquely identifies a place as within Google Maps

# for this assignment the following API endpoint must be used (it has a static subset of the Google Data):

# http://py4e-data.dr-chuck.net/json?
#  this API endpoint has a static subset of the Google Data 
# it uses the same parameter (address) as the Google API. 
# it also has no rate limit so you can test as often as you like.

# to call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter
# test to see if the program is working with a location of "South Federal University" 
# a place_id would be  "ChIJNeHD4p-540AR2Q0_ZjwmKJ8".

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

location = 'South Federal University'
url = serviceurl + urllib.parse.urlencode({'address': location, 'key' : 42})
print('Retrieving', url)
url_handle = urllib.request.urlopen(url)
data = url_handle.read().decode()
print('Retrieved', len(data), 'characters')

js_info = json.loads(data)
place_id = js_info['results'][0]['place_id']
print('The Place ID is: ', place_id)
