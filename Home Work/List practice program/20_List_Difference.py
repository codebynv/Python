# Find Elements Present in One List but Not Another

list1 = [10,20,30,40,50]

list2 = [30,40]

difference = []

for item in list1:
    if item not in list2:
        difference.append(item)

print("Difference =", difference)