def cart():
    items = []
    print("----Welcomes to shopping cart-----")

    total_item = int(input("Enter how many  iteme you want to add = "))

    for i in range(1,total_item+1):
        item_name = input(f"Enter item name {i}= ")
        items.append(item_name)

    print(f"you add item {items}")


    while True:
        operation = int(input("Enter 1-Add\n2-update\n3-Delete\n4-view\n5-Exit/stop"))

        if operation == 1:
            add = input("Enter item you wanto to add= ")
            items.append(add)
            print(f"Item {add} has been succesfully added... ")
        elif operation == 2:
            updated_val = input("Enter the item you want to updated =  ")
            if updated_val in items:
                up = input("Enter new item = ")
                ind = items.index(updated_val)
                items[ind] = up
                print(f"update item {up}")

        elif operation == 3:
            del_val = input("which item you want to Delete = ")
            if del_val in items:
                ind = items.index(del_val)
                del items[ind]
                print(f"item {del_val} has been delete....")

        elif operation ==4:
            print(f"Total item = {items}")

        elif operation == 5:
            print("closing the program...")
            break
        else:
            print("Invaild input")
cart()            
