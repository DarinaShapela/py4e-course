import urllib.request, urllib.parse, urllib.error 
import sqlite3
import json
import time
import ssl
import http

#api_key = 42
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

http.client.HTTPConnection.debuglevel = 1
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

fh = open("where.data")
count = 0
nofound = 0

for line in fh:
    address = line.strip()
    print('')
    cur.execute('''INSERT INTO Locations (address)
         VALUES ( ? )''', (address,))
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    conn.commit()

    if count > 100 :
        print('Retrieved 100 locations, restart to retrieve more')
        break


    try:
        data = cur.fetchone()[0]
        print("Found in database", address)
        continue
    except:
        pass

    parms = dict()
    parms['q'] = address

    # {
    #     "q":  ["Ikrutsk", "State"]
    # }

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        nofound = nofound + 1

    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

if nofound > 0:
    print('Number of features for which the location could not be found:', nofound)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
