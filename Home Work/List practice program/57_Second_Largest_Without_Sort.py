numbers = [45,12,78,23,9,56]

largest = second = -999999

for num in numbers:

    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

smallest = second_small = 999999

for num in numbers:

    if num < smallest:
        second_small = smallest
        smallest = num

    elif num < second_small and num != smallest:
        second_small = num

print("Second Largest :", second)

print("Second Smallest :", second_small)