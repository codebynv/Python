numbers = [10,20,30,40,50]

k = int(input("Enter Rotation: "))

print("Left :", numbers[k:] + numbers[:k])

print("Right :", numbers[-k:] + numbers[:-k])