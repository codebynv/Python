# Menu Driven List Operations

items = []

while True:

    print("\n===== MENU =====")
    print("1.Append")
    print("2.Insert")
    print("3.Extend")
    print("4.Remove")
    print("5.Pop")
    print("6.Sort")
    print("7.Reverse")
    print("8.Count")
    print("9.Index")
    print("10.Copy")
    print("11.Clear")
    print("12.Display")
    print("13.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        items.append(input("Item: "))

    elif choice == "2":
        pos = int(input("Position: "))
        item = input("Item: ")
        items.insert(pos, item)

    elif choice == "3":
        data = input("Enter Items: ").split()
        items.extend(data)

    elif choice == "4":
        item = input("Remove Item: ")
        if item in items:
            items.remove(item)

    elif choice == "5":
        if items:
            print("Removed:", items.pop())

    elif choice == "6":
        items.sort()

    elif choice == "7":
        items.reverse()

    elif choice == "8":
        item = input("Item: ")
        print(items.count(item))

    elif choice == "9":
        item = input("Item: ")
        if item in items:
            print(items.index(item))

    elif choice == "10":
        print(items.copy())

    elif choice == "11":
        items.clear()

    elif choice == "12":
        print(items)

    elif choice == "13":
        break