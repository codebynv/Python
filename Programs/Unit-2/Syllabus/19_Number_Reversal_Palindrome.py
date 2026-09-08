# Program 19
# Number Reversal and Palindrome

num = int(input("Enter Number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number =", reverse)

if original == reverse:
    print("Palindrome Number")
else:
    print("Not Palindrome")