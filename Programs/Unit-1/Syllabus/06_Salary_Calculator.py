# Program 06
# Salary Calculator

basic = float(input("Enter Basic Salary: "))

hra = basic * 0.20
da = basic * 0.10
pf = basic * 0.12

gross = basic + hra + da
net = gross - pf

print("\nHRA =", hra)
print("DA =", da)
print("PF =", pf)
print("Gross Salary =", gross)
print("Net Salary =", net)