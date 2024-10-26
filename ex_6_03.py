# Exercise 3: Encapsulate this code in a function named count, and gen- eralize it so that it accepts the string and the letter as arguments. 


word = input('Enter a word: ')
letter = input('Enter a letter: ')
counter = 0
for x_letter in word:
    if x_letter == letter:
        count = count + 1
        continue
        print(count)
        


