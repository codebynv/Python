# Program 21
# Armstrong Number Finder

num = int(input("Enter Number: "))

temp = num
digits = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")

print("\nArmstrong Numbers from 1 to 999")

for n in range(1, 1000):
    s = 0
    d = len(str(n))
    temp = n

    while temp > 0:
        digit = temp % 10
        s += digit ** d
        temp //= 10

    if s == n:
        print(n, end=" ")