import urllib.request, urllib.parse, urllib.error
import sqlite3
import json
import time

api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"

conn = sqlite3.connect("geodata.sqlite")
cur = conn.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS Locations (
    address TEXT 
    geodata TEXT 
    )"""
)

fname = 'where.data'
fh = open(fname)
count = 0
for line in fh:
    if count > 200:
        print("Retrieved 200 locations, restart to retrieve more")
        break

    address = line.strip()
    print("")
    cur.execute('INSERT OR IGNORE INTO Locations (address) VALUES ( ? )''', (address, ) )

    try:
        data = cur.fetchone() [0]
        print("Found in database ", address)
        continue
    except:
        pass

    url = serviceurl + urllib.parse.urlencode({'address': address, 'key' : 42})
    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters", data[:20].replace("\n", " "))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if "status" not in js or (js["status"] != "OK" and js["status"] != "ZERO_RESULTS"):
        print("==== Failure To Retrieve ====")
        print(data)
        break


print(
    "Run geodump.py to read the data from the database so you can vizualize it on a map."
)
