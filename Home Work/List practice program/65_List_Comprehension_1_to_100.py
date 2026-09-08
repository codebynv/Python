numbers=[i for i in range(1,101)]

print("Squares")
print([i*i for i in numbers])

print("\nCubes")
print([i**3 for i in numbers])

print("\nEven")
print([i for i in numbers if i%2==0])

print("\nOdd")
print([i for i in numbers if i%2!=0])

print("\nMultiples of 5")
print([i for i in numbers if i%5==0])