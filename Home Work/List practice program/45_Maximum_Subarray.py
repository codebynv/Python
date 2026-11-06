# Find the maximum sum of a non-empty contiguous subarray.

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

if not numbers:
    raise ValueError("The input list must not be empty.")

current_sum = best_sum = numbers[0]

for number in numbers[1:]:
    current_sum = max(number, current_sum + number)
    best_sum = max(best_sum, current_sum)

print("Maximum Subarray Sum :", best_sum)
