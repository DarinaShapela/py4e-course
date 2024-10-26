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
        word_lst.append(words[1])
        
for word in word_lst:
    mail_counts[word] = mail_counts.get(word,0) + 1

large_count = None
email = None
for k,v in mail_counts.items():
    if large_count is None or v > large_count:
        email = k
        large_count = v

print(email, large_count)