# Exercise 3: Write a program to read through a mail log, build a his- togram using a dictionary to count how many messages have come from each email address, and print the dictionary.

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

print(mail_counts)