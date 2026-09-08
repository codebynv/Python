numbers = list(range(1, 21))

result = []

for num in numbers:

    if num < 2:
        result.append(num)

    else:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if not prime:
            result.append(num)

print(result)