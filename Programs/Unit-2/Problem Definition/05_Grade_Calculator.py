# Grade Calculator

marks = float(input("Enter Marks (0-100): "))

if marks >= 90 and marks <= 100:

    print("Grade A")

elif marks >= 80:

    print("Grade B")

elif marks >= 70:

    print("Grade C")

elif marks >= 0:

    print("Fail")

else:

    print("Invalid Marks")