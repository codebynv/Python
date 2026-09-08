# Find All Pairs with Target Sum

numbers = [2, 4, 3, 5, 7, 8, 9]

target = int(input("Enter Target Sum: "))

print("Pairs:")

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])