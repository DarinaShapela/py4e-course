# Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

num = 0
total = 0
count = 0
average = 0
# The "while true" loop in python runs without any conditions until the break statement executes inside the loop.
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        number = int(num)
        total = total + number
        count = count + 1
        average = total / count

    except:
        print("Enter valid number or done")
        continue

print(total, count, average)
