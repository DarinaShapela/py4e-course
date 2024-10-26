fname = input("Enter file name: ")
fhandle = open(fname)

word_lst = list()
mail_counts = dict()

for line in fhandle:
    line = line.rstrip()
    words = line.split()
    if len(line) < 2 or words[0] != 'From':
        continue
    else:
        word = words[1]
        mail_counts[word] = mail_counts.get(word,0) + 1

large_count = None
email = None
for key,value in mail_counts.items():
    if large_count is None or value > large_count:
        email = key
        large_count = value

print(email, large_count)