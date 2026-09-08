cities = []

while True:

    print("\n1.Add")
    print("2.Display")
    print("3.Update")
    print("4.Delete")
    print("5.Exit")

    choice = input("Choice: ")

    if choice == "1":
        cities.append(input("City: "))

    elif choice == "2":
        print(cities)

    elif choice == "3":
        old = input("Old City: ")

        if old in cities:
            index = cities.index(old)
            cities[index] = input("New City: ")

    elif choice == "4":
        city = input("Delete City: ")

        if city in cities:
            cities.remove(city)

    elif choice == "5":
        break