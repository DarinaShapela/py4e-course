# Extracting Data from JSON exercise

# program should prompt for a URL, read the JSON data from URL using urllib;
# then parse and extract the comment counts from the JSON data;
# compute the sum of the numbers in the file and enter the sum below

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1774966.json (Sum ends with 4)

import urllib.request, urllib.parse, urllib.error
import json
count = 0
values = list()

url = 'http://py4e-data.dr-chuck.net/comments_42.json'
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