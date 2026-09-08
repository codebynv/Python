# Filter Numbers Divisible by 3 and 5

numbers = list(range(1, 101))

result = [num for num in numbers if num % 3 == 0 and num % 5 == 0]

print(result)