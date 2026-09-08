# Program 08
# Kilometer Converter

km = float(input("Enter Distance in Kilometers: "))

meters = km * 1000
centimeters = km * 100000
miles = km * 0.621371
feet = km * 3280.84         #formula gpt

print("\nMeters =", meters)
print("Centimeters =", centimeters)
print("Miles =", miles)
print("Feet =", feet)