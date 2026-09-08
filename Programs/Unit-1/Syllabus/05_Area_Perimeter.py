# Program 05
# Area and Perimeter of Rectangle + Area of Circle
#gpt 

import math

length = float(input("Enter Length: "))
breadth = float(input("Enter Breadth: "))

rectangle_area = length * breadth
perimeter = 2 * (length + breadth)

circle_area = math.pi * length ** 2

print("\nRectangle Area =", rectangle_area)
print("Rectangle Perimeter =", perimeter)
print("Circle Area =", circle_area)