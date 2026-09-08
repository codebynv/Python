# Split List into Chunks

numbers = [1,2,3,4,5,6,7,8,9,10]

size = int(input("Enter Chunk Size: "))

for i in range(0, len(numbers), size):
    print(numbers[i:i+size])