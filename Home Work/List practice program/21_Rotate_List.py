# Rotate List Left and Right

numbers = [10, 20, 30, 40, 50]

n = int(input("Enter Rotation Position: "))

left = numbers[n:] + numbers[:n]
right = numbers[-n:] + numbers[:-n]

print("Original List :", numbers)
print("Left Rotation :", left)
print("Right Rotation :", right)