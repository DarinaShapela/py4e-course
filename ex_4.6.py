# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. 

def computepay(hours, rate):
    multiplied1 = hours * rate
    multiplied2 = 40 * rate + ((hours - 40) * (rate * 1.5))
    if hours <= 40 : 
        return multiplied1
    if hours > 40 :
        return multiplied2

hrs = input("Enter Hours:")
h = float(hrs)
rt = input('Enter Rate:')
r = float(rt)
pay = computepay(h, r)
print('Pay', pay)