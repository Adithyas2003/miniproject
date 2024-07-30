class PetStore:
    def __init__(self):
        self.pets = []
        self.customers = []

    def add_pet(self, pet_name, pet_type, pet_price):
        self.pets.append({"name": pet_name, "type": pet_type, "price": pet_price})
        print(f"Added pet {pet_name} ({pet_type}) for ${pet_price:.2f}.")

    def show_inventory(self):
        print("\nCurrent Inventory:")
        if not self.pets:
            print("No pets available.")
        for pet in self.pets:
            print(f"Name: {pet['name']}, Type: {pet['type']}, Price: ${pet['price']:.2f}")

    def add_customer(self, customer_name):
        self.customers.append(customer_name)
        print(f"Added customer {customer_name}.")

    def show_customers(self):
        print("\nCustomer List:")
        if not self.customers:
            print("No customers added.")
        for customer in self.customers:
            print(customer)

    def sell_pet(self, pet_name):
        for pet in self.pets:
            if pet['name'].lower() == pet_name.lower():
                self.pets.remove(pet)
                print(f"Sold pet {pet_name}.")
                return True
        print(f"Pet {pet_name} not found.")
        return False

def main():
    store = PetStore()
    
    while True:
        print("\nPet Store Management System")
        print("1. Add Pet")
        print("2. Show Inventory")
        print("3. Add Customer")
        print("4. Show Customers")
        print("5. Sell Pet")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            pet_name = input("Enter pet name: ")
            pet_type = input("Enter pet type (e.g., Cat, Dog): ")
            try:
                pet_price = float(input("Enter pet price: "))
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
                continue
            store.add_pet(pet_name, pet_type, pet_price)
        elif choice == '2':
            store.show_inventory()
        elif choice == '3':
            customer_name = input("Enter customer's name: ")
            store.add_customer(customer_name)
        elif choice == '4':
            store.show_customers()
        elif choice == '5':
            pet_name = input("Enter pet name to sell: ")
            store.sell_pet(pet_name,customer_name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()