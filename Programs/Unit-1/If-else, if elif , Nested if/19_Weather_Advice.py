# Program 19
# Give weather advice based on temperature

temp = float(input("Enter Temperature: "))

if temp > 35:
    print("It's very hot!")
elif temp >= 20:
    print("The weather is pleasant.")
else:
    print("It's cold outside.")