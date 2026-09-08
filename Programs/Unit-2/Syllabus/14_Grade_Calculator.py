# Program 14
# Grade Calculator

marks = float(input("Enter Marks: "))

if marks >= 90:
    print("Grade : A+")
    print("Distinction")
elif marks >= 80:
    print("Grade : A")
elif marks >= 70:
    print("Grade : B")
elif marks >= 60:
    print("Grade : C")
elif marks >= 35:
    print("Grade : D")
else:
    print("Fail")