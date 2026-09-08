# Swap Two Elements

numbers = [10, 20, 30, 40, 50]

print("Original List :", numbers)

pos1 = int(input("Enter First Position: "))
pos2 = int(input("Enter Second Position: "))

numbers[pos1], numbers[pos2] = numbers[pos2], numbers[pos1]

print("Updated List :", numbers)