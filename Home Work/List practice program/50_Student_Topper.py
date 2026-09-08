# Student Details

students = [
    [101, "Ram", 75],
    [102, "Shyam", 92],
    [103, "Mohan", 85]
]

topper = students[0]

for student in students:

    if student[2] > topper[2]:
        topper = student

print("Topper Details")

print("Roll No :", topper[0])

print("Name :", topper[1])

print("Marks :", topper[2])

students.sort(key=lambda x: x[2], reverse=True)

print("\nSorted Students")

for student in students:
    print(student)