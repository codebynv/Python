# Program 10
# BMI Calculator
#formula by gpt

weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))

bmi = weight / (height ** 2)

print("\nBMI =", round(bmi, 2))

if bmi < 18.5:
    print("Category : Underweight")
elif bmi < 25:
    print("Category : Normal")
elif bmi < 30:
    print("Category : Overweight")
else:
    print("Category : Obese")