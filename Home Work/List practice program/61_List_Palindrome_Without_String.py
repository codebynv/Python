numbers = [1,2,3,2,1]

left = 0
right = len(numbers)-1

palindrome = True

while left < right:

    if numbers[left] != numbers[right]:
        palindrome = False
        break

    left += 1
    right -= 1

if palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")