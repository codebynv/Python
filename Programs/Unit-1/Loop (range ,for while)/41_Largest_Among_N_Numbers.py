# Program 41
# Largest Among N Numbers

n = int(input("How Many Numbers? "))

largest = float("-inf")

for i in range(n):
    num = float(input("Enter Number: "))

    if num > largest:
        largest = num

print("Largest Number =", largest)