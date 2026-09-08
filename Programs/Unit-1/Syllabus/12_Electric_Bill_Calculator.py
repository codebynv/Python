# Program 12
# Electric Bill Calculator

previous = float(input("Enter Previous Meter Reading: "))
current = float(input("Enter Current Meter Reading: "))

units = current - previous
fixed_charge = 100
bill = (units * 5.50) + fixed_charge

print("\nUnits Consumed =", units)
print("Total Bill =", bill)