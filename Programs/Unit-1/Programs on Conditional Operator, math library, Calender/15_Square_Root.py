# Program 15
# Find Square Root of a Number
#gpt

import math

num = float(input("Enter a Number: "))

if num >= 0:
    root = math.sqrt(num)
    print("Square Root =", root)
else:
    print("Square Root of a Negative Number is Not Possible.")