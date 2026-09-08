# Menu Driven Area Calculator

import math

while True:

    print("\n===== Area Menu =====")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "4":
        print("Program Ended")
        break

    if choice == "1":

        length = float(input("Enter Length: "))
        breadth = float(input("Enter Breadth: "))

        area = length * breadth

        print("Area of Rectangle =", area)

    elif choice == "2":

        radius = float(input("Enter Radius: "))

        area = math.pi * radius ** 2

        print("Area of Circle =", round(area, 2))

    elif choice == "3":

        base = float(input("Enter Base: "))
        height = float(input("Enter Height: "))

        area = 0.5 * base * height

        print("Area of Triangle =", area)

    else:
        print("Invalid Choice")