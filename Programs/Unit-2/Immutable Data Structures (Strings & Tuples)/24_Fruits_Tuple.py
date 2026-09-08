# Program 24
# Fruits Tuple

fruits = ("Apple", "Banana", "Cherry", "Apple", "Mango")

print("Apple Count :", fruits.count("Apple"))

print("Cherry Index :", fruits.index("Cherry"))

fruit_list = list(fruits)

fruit_list.append("Orange")

fruits = tuple(fruit_list)

print("Updated Tuple :", fruits)