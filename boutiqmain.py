# main.py

import boutique

def main():
    while True:
        print("\nBoutique Management System")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Place Order")
        print("4. Display Orders")
        print("5. Calculate Revenue")
        print("6. Reset System")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            boutique.add_product(name, price, stock)

        elif choice == '2':
            boutique.display_products()

        elif choice == '3':
            product_name = input("Enter product name to order: ")
            quantity = int(input("Enter quantity: "))
            boutique.place_order(product_name, quantity)

        elif choice == '4':
            boutique.display_orders()

        elif choice == '5':
            boutique.calculate_revenue()

        elif choice == '6':
            boutique.reset_system()

        elif choice == '7':
            print("Exiting Boutique Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
