numbers = [2,4,7,8,10]

missing=[]

for i in range(min(numbers),max(numbers)+1):
    if i not in numbers:
        missing.append(i)

print(missing)