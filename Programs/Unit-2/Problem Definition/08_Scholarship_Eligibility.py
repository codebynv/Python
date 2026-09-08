# Scholarship Eligibility

gpa = float(input("Enter GPA: "))
failed = int(input("Number of Failed Subjects: "))
activity = input("Participated in Extracurricular Activity? (yes/no): ").lower()

if gpa >= 3.5 and failed == 0 and activity == "yes":
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")