landreg=[]
while True:
    print("Land Registration")
    print("1.Register a new land")
    print("2.View Registration")
    print("3.Exit")
    ch=input("enter Your Choice:")

    if ch == '1':
        owner = input("Enter The Owner's Name: ")
        size = input("Enter The Size Of Land: ")
        location = input("Enter The Location Of Land: ")
        if owner and size and location:
            landpar = {'owner': owner, 'size': size, 'location': location}  
            landreg.append(landpar)
            print("Land parcel registered successfully.")
    
    elif ch == '2':
        if not landreg:
            print("No land parcels registered.")
        else:
            for index, parcel in enumerate(landreg, start=1):
                print(f"Parcel {index}:")
                print(f"Owner: {parcel['owner']}")
                print(f"Size: {parcel['size']}")
                print(f"Location: {parcel['location']}")
                print()
   
    elif ch == '3':
        print("Exiting The System.")
        break

    else:
        print("Invalid choice. Please try again.")