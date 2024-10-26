fname = input('Enter file name: ')
fhandle = open(fname)
hours_counted = {}

for line in fhandle:
    line = line.rstrip()
    words = line.split()
    if len(line) < 2 or words[0] != 'From':
        continue
    else:
        time = words[5]
        time_pieces = time.split(':')
        hour = time_pieces[0]
        hours_counted[hour] = hours_counted.get(hour, 0) +1

data = sorted(hours_counted.items())
for k,v in data:
    print(k,v)