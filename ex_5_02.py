# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

num = 0
largest = None
smallest = None

while True :
    num = input('Enter a number: ')
    if num == 'done' :
        break
    try :
        number = int(num)
        if largest is None or number > largest :
            largest = number
        
        if smallest is None or number < smallest :
            smallest = number
            
    except :
        print('Invalid input')
        continue
        
print('Maximum is', largest)
print ('Minimum is', smallest)

        