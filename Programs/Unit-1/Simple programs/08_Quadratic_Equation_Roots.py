# Program 08
# Calculate Roots of Quadratic Equation
#GPT CODE
import math

a = float(input("Enter Value of a: "))
b = float(input("Enter Value of b: "))
c = float(input("Enter Value of c: "))

d = b ** 2 - 4 * a * c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)       #dvighat smikaran avtu ht ej chhe
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif d == 0:
    root = -b / (2 * a)
    print("Both Roots =", root)

else:
    print("Imaginary Roots")