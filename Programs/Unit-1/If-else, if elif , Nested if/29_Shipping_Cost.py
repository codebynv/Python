# Program 29
# Shipping Cost Calculator

weight = float(input("Enter Weight (Kg): "))
destination = input("Destination (domestic/international): ").lower()

if destination == "domestic":
    if weight < 1:
        cost = 5
    elif weight <= 5:
        cost = 10
    elif weight <= 10:
        cost = 25
    else:
        cost = 50

elif destination == "international":
    if weight < 1:
        cost = 15
    elif weight <= 5:
        cost = 25
    elif weight <= 10:
        cost = 50
    else:
        cost = 75

else:
    cost = 0
    print("Invalid Destination")

if cost > 0:
    print("Shipping Cost = $", cost)