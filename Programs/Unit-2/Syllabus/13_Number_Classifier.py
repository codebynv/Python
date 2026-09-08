# Program 13
# Number Classifier

num = int(input("Enter a Number: "))

# Positive / Negative / Zero
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# Even / Odd
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Divisible by 5
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")