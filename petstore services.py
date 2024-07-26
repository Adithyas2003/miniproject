# class pet:
#     def _init_(s):
#         print("Register")
#     def name(s):
#         print("Enter the pet name")
#     def age(s):
#         print("Enter the age")
#     def species(s):
#         print("Enter the species")
#     def __str__(s):
#         return f"{s.species}:{s.name},{s.age}"
# class Dog(pet):
#     print("Dog Details")
#     def Dog_name(s):
#         print("Enter Dog name")
#     def Dog_age(s):
#         print("Enter the Dog age")
#     def Dog_breed(s):
#         print("Enter the breed")
# class cat(pet):
#     print("cat details")
#     def cat_name(s):
#         print("Enter the  cat name")
#     def cat_    
    

class Pet:
    def __init__(s, name, age, species):
        s.name = name
        s.age = age
        s.species = species

    def __str__(s):
        return f"{s.species}: {s.name}, Age: {s.age}"

class Dog(Pet):
    def __init__(s, name, age, breed):
        super().__init__(name, age, "Dog")
        s.breed = breed

    def __str__(s):
        return f"Dog: {s.name}, Age: {s.age}, Breed: {s.breed}"

class Cat(Pet):
    def __init__(s, name, age, color):
        super().__init__(name, age, "Cat")
        s.color = color

    def __str__(s):
        return f"Cat: {s.name}, Age: {s.age}, Color: {s.color}"

class Customer:
    def __init__(s, name):
        s.name = name
        s.pets = []

    def adopt_pet(s, pet):
        s.pets.append(pet)

    def __str__(self):
        pet_list = ', '.join([str(pet) for pet in self.pets])
        return f"Customer: {self.name}, Pets: {pet_list if pet_list else 'None'}"

class PetStore:
    def __init__(s):
        s.inventory = []
        s.customers = []

    def add_pet(s, pet):
        s.inventory.append(pet)

    def add_customer(s, customer):
        s.customers.append(customer)

    def show_inventory(s):
        if not s.inventory:
            print("No pets in inventory.")
        for pet in s.inventory:
            print(pet)

    def show_customers(s):
        if not s.customers:
            print("No customers.")
        for customer in s.customers:
            print(customer)

    def sell_pet(s, customer_name, pet_name):
        customer = next((cust for cust in s.customers if cust.name == customer_name), None)
        pet = next((pt for pt in s.inventory if pt.name == pet_name), None)
        if customer and pet:
            customer.adopt_pet(pet)
            s.inventory.remove(pet)
            print(f"{customer_name} has adopted {pet_name}")
        else:
            print("Customer or pet not found")

# Example usage
pet_store = PetStore()

def menu():
    print("\nPet Store Menu:")
    print("1. Add Pet")
    print("2. Add Customer")
    print("3. Show Inventory")
    print("4. Show Customers")
    print("5. Sell Pet")
    print("6. Exit")

def add_pet():
    species = input("Enter pet species (Dog/Cat): ")
    name = input("Enter pet name: ")
    age = int(input("Enter pet age: "))
    if species.lower() == "dog":
        breed = input("Enter dog breed: ")
        pet_store.add_pet(Dog(name, age, breed))
    elif species.lower() == "cat":
        color = input("Enter cat color: ")
        pet_store.add_pet(Cat(name, age, color))
    else:
        print("Invalid species")

def add_customer():
    name = input("Enter customer name: ")
    pet_store.add_customer(Customer(name))

def show_inventory():
    print("\nInventory:")
    pet_store.show_inventory()

def show_customers():
    print("\nCustomers:")
    pet_store.show_customers()

def sell_pet():
    customer_name = input("Enter customer name: ")
    pet_name = input("Enter pet name: ")
    pet_store.sell_pet(customer_name, pet_name)

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_pet()
    elif choice == '2':
        add_customer()
    elif choice == '3':
        show_inventory()
    elif choice == '4':
        show_customers()
    elif choice == '5':
        sell_pet()
    elif choice == '6':
        break
    else:
        print("Invalid choice, please try again.")




    

