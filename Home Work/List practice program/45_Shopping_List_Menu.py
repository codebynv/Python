# Shopping List Menu

items = []

while True:

    print("\n1.Add")
    print("2.Remove")
    print("3.Search")
    print("4.Update")
    print("5.Sort")
    print("6.Display")
    print("7.Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        items.append(input("Item : "))

    elif choice == "2":
        item = input("Remove Item : ")
        if item in items:
            items.remove(item)

    elif choice == "3":
        item = input("Search Item : ")
        if item in items:
            print("Found")
        else:
            print("Not Found")

    elif choice == "4":
        old = input("Old Item : ")
        if old in items:
            index = items.index(old)
            items[index] = input("New Item : ")

    elif choice == "5":
        items.sort()

    elif choice == "6":
        print(items)

    elif choice == "7":
        break