# Program 05
# Convert Kilometer to Meter, Centimeter, Inch and Foot

km = float(input("Enter Distance in Kilometer: "))


#formulas
meter = km * 1000
centimeter = km * 100000

#gpt
inch = km * 39370.1
foot = km * 3280.84

print("Meter =", meter)
print("Centimeter =", centimeter)
print("Inch =", inch)
print("Foot =", foot)