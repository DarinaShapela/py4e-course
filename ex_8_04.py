fname = input("Enter file name: ")
fh = open(fname)
main_lst = list()
for line in fh:
    word_lst = line.split()
    for word in word_lst:
        if word not in main_lst:
            main_lst.append(word)
            
main_lst.sort()
print(main_lst)