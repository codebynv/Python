# Employee Search and Update

employees = ["Ram", "Shyam", "Mohan"]

name = input("Enter Employee Name : ")

if name in employees:

    index = employees.index(name)

    employees[index] = input("Enter New Name : ")

else:

    employees.append(name)

print(employees)