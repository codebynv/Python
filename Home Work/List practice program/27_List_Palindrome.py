# Check whether a list reads the same forward and backward.

numbers = [1, 2, 3, 2, 1]

left = 0
right = len(numbers) - 1
is_palindrome = True

while left < right:
    if numbers[left] != numbers[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print("Palindrome List" if is_palindrome else "Not a Palindrome List")
