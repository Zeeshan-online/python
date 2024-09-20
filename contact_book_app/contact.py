contacts = {}

while True:
    print("\nContact Book App")
    print("1. create contact")
    print("2. view contact")
    print("3. update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contact")
    print("7. Exit ")

    choice = input("Enter the your choice = ")
    if choice == '1':
        name = input("Enter Name = ")
        if name in contacts:
            print(f"Enter you name {name} already exist!")
        else:
            age = input("Enter age = ")
            email = input("Enter Email = ")
            mobile = input("Enter Mobile number = ")
            contacts[name] = {"age": int(age), "email":email, 'moblie': mobile}
            print(f"Conatct name {name} has been created successfully")
    elif choice == '2':
        name = input("Enter the name to view = ")
        if name in contacts:
            contact = contacts[name]
            print(f'Name:{name}, Age:{ age}, mobile number:{mobile}')
        else:
            print("contact not found")
    elif choice == '3':
        name = input("Enter the name to update = ")
        if name in contact:
            age = input("Enter updated age = ")
            email = input("Enter updated email")
            mobile = input("Enter updated mobile number = ")
            contacts[name] = { 'Name:(name), Age:{age}, mobile number:{mobile}'}
        else:
            print("contact not found")
    elif choice == '4':
        name = input("Enter contact ane to delete = ")
        if name in contacts:
            del contacts[name]
            print(f"conatct name {name} has been deleted succefuly")
        else:
            print("contact not found")
    elif choice == '5':
        name = input("Enter the name search = ")
        if name in contacts:
            search_name = input("Enter contact name to search = ")
            found = False
            for name, contacts in contacts.items():
                if search_name.lower() in name.lower():
                   print(f'Found - Name {name}, Age:{age}, mobile number:{mobile}, Email:{email} ')
                   found = True
            if not found:
                print("contact no found")       
    elif choice == "6":
        print(f"Total contact in your book : {len(contacts)}")

    elif choice == '7':
        print("closing the programe")
        break
    else:
        print("Invalid in input")                
                    



