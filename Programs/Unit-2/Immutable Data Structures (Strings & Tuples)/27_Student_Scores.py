# Program 27
# Student Scores

scores = (85, 78, 92, 88, 95, 72, 80)

average = sum(scores) / len(scores)

print("Average :", average)

count = 0

for mark in scores:
    if mark > 80:
        count += 1

print("Students Above 80 :", count)

top = tuple(sorted(scores, reverse=True)[:3])

print("Top Three Scores :", top)