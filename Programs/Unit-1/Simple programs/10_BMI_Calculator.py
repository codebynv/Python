# Program 10
# Calculate Body Mass Index (BMI)
#gpt kryu formula bs 

weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))

bmi = weight / (height ** 2)

print("BMI =", round(bmi, 2))