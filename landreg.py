
landreg = []

credentials = {}

# Registration:
while True:
    print("Registration:")
    reg_username = input("Choose a Username: ")
    reg_password = input("Choose a Password: ")

    if reg_username in credentials:
        print("Username already exists. Please choose another one.\n")
    else:
        credentials[reg_username] = reg_password
        print("Registration successful.\n")
        break  

# Login:
while True:
    print("Login:")
    uname = input("Username: ")
    pwd = input("Password: ")

    if uname in credentials and credentials[uname] == pwd:
        print("Login successful.\n")
        break  
    else:
        print("Invalid username or password. Please try again.\n")

# Main menu:
logged_in = True  

while logged_in:
    print("Land Registration")
    print("1. Register a new land")
    print("2. View Registration")
    print("3. Logout")
    print("4. Exit")
    ch = input("Enter Your Choice: ")

    if ch == '1':
        owner = input("Enter The Owner's Name: ")
        size = input("Enter The Size Of Land: ")
        location = input("Enter The Location Of Land: ")

        if owner and size and location:
            landpar = {'owner': owner, 'size': size, 'location': location}
            landreg.append(landpar)
            print("Land parcel registered successfully.\n")
        else:
            print("Error: Please provide all details (Owner Name, Size, Location).\n")

    elif ch == '2':
        if not landreg:
            print("No land parcels registered.\n")
        else:
            for index, parcel in enumerate(landreg, start=1):
                print(f"Parcel {index}:")
                print(f"Owner: {parcel['owner']}")
                print(f"Size: {parcel['size']}")
                print(f"Location: {parcel['location']}")
                print()

    elif ch == '3':
        print("Logging out.\n")
        logged_in = False  

    elif ch == '4':
        print("Exiting The System.")
        logged_in = False  
        break

    else:
        print("Invalid choice. Please try again.\n")