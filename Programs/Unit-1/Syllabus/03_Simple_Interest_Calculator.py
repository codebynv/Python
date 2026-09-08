# Program 03
# Simple Interest Calculator

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate (%): "))
time = float(input("Enter Time (Years): "))

si = (principal * rate * time) / 100
amount = principal + si

print("\nSimple Interest =", si)
print("Total Amount =", amount)