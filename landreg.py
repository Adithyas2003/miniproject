
print('LAND REGISTRATION SYSTEM')

# Hardcoded admin credentials for simplicity
admin_username = 'admin'
admin_password = 'password'

# Hardcoded user credentials
users = [{'username': 'anu', 'password': '7676'}]

plots = []
plot_id_counter = 1  # Counter for generating unique plot IDs

authenticated = False

while not authenticated:
    username = input("\nEnter username: ")
    password = input("Enter password: ")

    # Check if the entered username and password match admin credentials
    if username == admin_username and password == admin_password:
        authenticated = True
        print("Admin login successful!")
        break

    # Check if the entered username and password match any user credentials
    for user in users:
        if user['username'] == username and user['password'] == password:
            authenticated = True
            print("User login successful!")
            break

    if not authenticated:
        print("Invalid username or password. Please try again.")

# Once authenticated, proceed to the main menu
while True:
    print("\n1. Register a new plot")
    print("2. View details of a plot")
    print("3. Update plot details")
    print("4. Display all plots")
    print("5. Buy a plot")
    print("6. Exit")

    choice = input("\nEnter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        # Register a new plot
        print("\nEnter details for the new plot:")
        plot = {}
        plot['plot_id'] = plot_id_counter
        plot['owner'] = input("Owner's name: ")

        # Validate area input
        valid_area = False
        while not valid_area:
            area_input = input("Area of the plot (in square meters): ")
            if area_input.isdigit() and int(area_input) > 0:
                plot['area'] = float(area_input)
                valid_area = True
            else:
                print("Invalid input. Please enter a valid positive number for area.")

        # Validate value input
        valid_value = False
        while not valid_value:
            value_input = input("Estimated value of the plot (in dollars): ")
            if value_input.isdigit() and int(value_input) > 0:
                plot['value'] = float(value_input)
                valid_value = True
            else:
                print("Invalid input. Please enter a valid positive number for value.")

        plots.append(plot)
        plot_id_counter += 1
        print("Plot registered successfully!")

    elif choice == '2':
        # View details of a specific plot
        if not plots:
            print("No plots registered yet.")
        else:
            plot_id = int(input("Enter plot ID to view details: "))
            plot_found = False
            for plot in plots:
                if plot['plot_id'] == plot_id:
                    print("\nPlot Details:")
                    print(f"Plot ID: {plot['plot_id']}")
                    print(f"Owner: {plot['owner']}")
                    print(f"Area: {plot['area']} sqm")
                    print(f"Value: ${plot['value']}")
                    plot_found = True
                    break
            if not plot_found:
                print(f"Plot with ID {plot_id} not found.")

    elif choice == '3':
        # Update plot details
        if not plots:
            print("No plots registered yet.")
        else:
            plot_id = int(input("Enter plot ID to update details: "))
            plot_found = False
            for plot in plots:
                if plot['plot_id'] == plot_id:
                    print("\nCurrent Plot Details:")
                    print(f"Plot ID: {plot['plot_id']}")
                    print(f"Owner: {plot['owner']}")
                    print(f"Area: {plot['area']} sqm")
                    print(f"Value: ${plot['value']}")
                    print("\nEnter new details for the plot:")
                    plot['owner'] = input("New owner's name (press Enter to keep current): ") or plot['owner']

                    # Validate new area input
                    valid_area = False
                    while not valid_area:
                        new_area_input = input("New area of the plot (in square meters, press Enter to keep current): ")
                        if new_area_input == '':
                            break
                        elif new_area_input.isdigit() and int(new_area_input) > 0:
                            plot['area'] = float(new_area_input)
                            valid_area = True
                        else:
                            print("Invalid input. Please enter a valid positive number for area.")

                    # Validate new value input
                    valid_value = False
                    while not valid_value:
                        new_value_input = input("New estimated value of the plot (in dollars, press Enter to keep current): ")
                        if new_value_input == '':
                            break
                        elif new_value_input.isdigit() and int(new_value_input) > 0:
                            plot['value'] = float(new_value_input)
                            valid_value = True
                        else:
                            print("Invalid input. Please enter a valid positive number for value.")

                    print("Plot details updated successfully!")
                    plot_found = True
                    break
            if not plot_found:
                print(f"Plot with ID {plot_id} not found.")

    elif choice == '4':
        # Display all registered plots
        print("\nAll Registered Plots:")
        if not plots:
            print("No plots registered yet.")
        else:
            for plot in plots:
                print(f"Plot ID: {plot['plot_id']}, Owner: {plot['owner']}, Area: {plot['area']} sqm, Value: ${plot['value']}")

    elif choice == '5':
        # Buy a plot
        if not plots:
            print("No plots available to buy.")
        else:
            plot_id = int(input("Enter plot ID to buy: "))
            plot_found = False
            for plot in plots:
                if plot['plot_id'] == plot_id:
                    print("\nBuying Plot Details:")
                    print(f"Plot ID: {plot['plot_id']}")
                    print(f"Owner: {plot['owner']}")
                    print(f"Area: {plot['area']} sqm")
                    print(f"Value: ${plot['value']}")
                    confirm = input("Confirm purchase (yes/no): ").lower()
                    if confirm == 'yes':
                        plots.remove(plot)
                        print("Plot purchased successfully!")
                    else:
                        print("Purchase cancelled.")
                    plot_found = True
                    break
            if not plot_found:
                print(f"Plot with ID {plot_id} not found.")

    elif choice == '6':
        # Exit the program
        print("Exiting the Land Registration System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, 4, 5, or 6.")