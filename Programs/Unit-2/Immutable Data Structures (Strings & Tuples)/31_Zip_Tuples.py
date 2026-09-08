# Program 31
# Zip Tuples
#need to understande
names = ("Alice", "Bob", "Charlie")
scores = (85, 78, 92)

students = tuple(zip(names, scores))

print("Zipped Tuple :")
print(students)

highest = max(scores)

index = scores.index(highest)

print("\nHighest Scorer :", names[index])

name_tuple, score_tuple = zip(*students)

print("\nNames :", name_tuple)
print("Scores :", score_tuple)