hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
pay = h * r
if h > 40:
    pay = 40 * r
    hrs2 = h - 40
    r2 = r * 1.5
    pay2 = hrs2 * r2
    payf = pay + pay2
    print(payf)
else:
    print(pay)
