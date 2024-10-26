# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

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
        piece = word.split('@')
        domain = piece[1]
        mail_counts[domain] = mail_counts.get(domain,0) + 1

print(mail_counts)