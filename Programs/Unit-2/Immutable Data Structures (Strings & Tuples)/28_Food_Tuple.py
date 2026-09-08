# Program 28
# Food Tuple

food = ("Pizza", "Burger", "Pasta")

print("Original Tuple :", food)

print("\nTuple cannot be modified because it is immutable.")

food_list = list(food)

food_list[0] = "Sandwich"

food = tuple(food_list)

print("Updated Tuple :", food)

print("Burger Index :", food.index("Burger"))