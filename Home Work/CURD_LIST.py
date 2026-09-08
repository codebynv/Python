items = []

while True:
    print("\n===========LIST CURD OPERATION============")
    print("1 For Add in List")
    print("2 For Display List")
    print("3 For Update List")
    print("4 For Searching In List")
    print("5 for delete in list")
    print("6 for exit")

    choice = int(input("\nEnter Your Choice"))

    if choice == 1:
        print("Your Selected Choice is Add In List")
        one = input("\n Enter a value ")
        items.append(one)

    elif choice == 2:
        print("Your Selected Choice is Display List")
        if len(items) == 0:
            print("List Is Empty")
        else:
            print(items)

    elif choice == 3:
        print("Your Selected Choice is Update List")
        if len(items) == 0:
            print("List Is Empty")
        else:
            print(items)

            ind = int(input("Enter the Index you want to update: "))

            if 0 <= ind < len(items):
                upd = input("Enter the new value: ")
                items[ind] = upd
                print("Updated List:", items)
            else:
                print("Invalid Index!")

    elif(choice == 4):
        print("Your Selected Choice is Searching In List")
        if(len(items) == 0):
                print("List is Empty")
        else:
            print(items)           
            search = input("Enter the value you want to search: ")
            if search in items:
                print("Value found in the list.")
            else:
                print("Value not found in the list.")

    elif(choice == 5):
        print("Your Selected Choice is Delete In List")
        if(len(items) == 0):
            print("List is Empty")
        else:
            print(items)
            delete_item = input("Enter the value you want to delete: ")
            if delete_item in items:
                items.remove(delete_item)
                print("Value deleted from the list.")
            else:
                print("Value not found in the list.")

    elif choice == 6:
        break

    else:
        print("Enter a valid choice")