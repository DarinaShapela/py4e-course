# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.


name = 'Naerys'
index = len(name)-1
while index >= 0:
    letter = name[index]
    print(letter)
    index = index -1
    if index < 0:
        quit()