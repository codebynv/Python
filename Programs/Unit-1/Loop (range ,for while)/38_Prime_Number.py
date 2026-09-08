# Program 38
# Check Prime Number

num = int(input("Enter a Number: "))

if num <= 1:
    print("Not Prime")
else:
    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not Prime")