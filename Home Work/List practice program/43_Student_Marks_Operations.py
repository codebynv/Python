# Student Marks Operations

marks = [75, 88, 92, 65, 81, 70, 95, 60, 78, 85]

print("Original Marks :", marks)

marks.append(90)

marks.remove(60)

marks[0] = 80

marks.sort()

print("Sorted Marks :", marks)

marks.reverse()

print("Reverse :", marks)

print("Highest :", max(marks))

print("Lowest :", min(marks))

print("Average :", sum(marks) / len(marks))