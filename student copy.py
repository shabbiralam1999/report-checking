# Electricity Bill Calculator

units = float(input("Enter total units consumed: "))

bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 8
else:
    bill = (100 * 5) + (100 * 8) + (units - 200) * 10

print("Your electricity bill is:", bill)
