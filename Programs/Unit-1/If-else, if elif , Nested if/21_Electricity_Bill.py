# Program 21
# Calculate Electricity Bill

units = float(input("Enter Units Consumed: "))

if units <= 100:
    bill = units * 0.5
elif units <= 200:
    bill = (100 * 0.5) + ((units - 100) * 0.75)
else:
    bill = (100 * 0.5) + (100 * 0.75) + ((units - 200) * 1.2)

print("Electricity Bill = $", bill)