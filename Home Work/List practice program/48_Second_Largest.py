# Find the second-largest distinct number without sorting the list.

numbers = [12, 35, 1, 10, 34, 35, 10]

largest = second_largest = None

for number in numbers:
    if largest is None or number > largest:
        if number != largest:
            second_largest = largest
            largest = number
    elif number != largest and (second_largest is None or number > second_largest):
        second_largest = number

if second_largest is None:
    print("A second distinct largest value does not exist.")
else:
    print("Second Largest Distinct Value :", second_largest)
