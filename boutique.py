# Global variables to store data
products = []
orders = []

# Function to add a product to inventory
def add_product(name, price, stock):
    products.append({'name': name, 'price': price, 'stock': stock})
    print(f"Product '{name}' added to inventory.")

# Function to display all products
def display_products():
    if not products:
        print("No products available.")
    else:
        print("Available Products:")
        for product in products:
            print(f"Name: {product['name']}, Price: ${product['price']}, Stock: {product['stock']}")

# Function to place an order
def place_order(product_name, quantity):
    for product in products:
        if product['name'] == product_name:
            if product['stock'] >= quantity:
                order_cost = product['price'] * quantity
                orders.append({'product': product_name, 'quantity': quantity, 'total_cost': order_cost})
                product['stock'] -= quantity
                print(f"Order placed for {quantity} units of '{product_name}'. Total cost: ${order_cost}")
            else:
                print(f"Sorry, '{product_name}' is out of stock.")
            return
    print(f"Product '{product_name}' not found in inventory.")

# Function to display all orders
def display_orders():
    if not orders:
        print("No orders placed yet.")
    else:
        print("Orders:")
        for order in orders:
            print(f"Product: {order['product']}, Quantity: {order['quantity']}, Total Cost: ${order['total_cost']}")

# Function to calculate total revenue
def calculate_revenue():
    total_revenue = sum(order['total_cost'] for order in orders)
    print(f"Total Revenue: ${total_revenue}")

# Function to reset boutique system (clear all data)
def reset_system():
    global products, orders
    products = []
    orders = []
    print("Boutique system has been reset.")




