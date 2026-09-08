students=[]

while True:

    print("\n1.Add")
    print("2.Display")
    print("3.Search")
    print("4.Update")
    print("5.Delete")
    print("6.Sort by Name")
    print("7.Sort by Marks")
    print("8.Topper")
    print("9.Average")
    print("10.Exit")

    choice=input("Choice: ")

    if choice=="1":
        name=input("Name: ")
        marks=float(input("Marks: "))
        students.append([name,marks])

    elif choice=="2":
        print(students)

    elif choice=="3":
        name=input("Search Name: ")
        for s in students:
            if s[0]==name:
                print(s)

    elif choice=="4":
        name=input("Update Name: ")
        for s in students:
            if s[0]==name:
                s[1]=float(input("New Marks: "))

    elif choice=="5":
        name=input("Delete Name: ")
        for s in students:
            if s[0]==name:
                students.remove(s)
                break

    elif choice=="6":
        students.sort()

    elif choice=="7":
        students.sort(key=lambda x:x[1],reverse=True)

    elif choice=="8":
        if students:
            print(max(students,key=lambda x:x[1]))

    elif choice=="9":
        if students:
            total=0
            for s in students:
                total+=s[1]
            print("Average =",total/len(students))

    elif choice=="10":
        break