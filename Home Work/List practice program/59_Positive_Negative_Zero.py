numbers = [10,-5,0,7,-2,8,0,-1]

positive = []
negative = []
zero = []

for num in numbers:

    if num > 0:
        positive.append(num)

    elif num < 0:
        negative.append(num)

    else:
        zero.append(num)

print("Positive :", positive)
print("Negative :", negative)
print("Zero :", zero)