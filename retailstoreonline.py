import sqlite3

con = sqlite3.connect("retailstore.db")

def create_tables():
    try:
        con.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                email TEXT,
                password TEXT
            )
        """)

        # Ensure the `password` column is present in case of schema changes
        try:
            con.execute("ALTER TABLE users ADD COLUMN password TEXT")
        except sqlite3.OperationalError:
            # Column already exists, do nothing
            pass

        con.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                price REAL,
                stock INTEGER
            )
        """)

        con.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                order_date TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)

        con.execute("""
            CREATE TABLE IF NOT EXISTS order_items (
                order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY (order_id) REFERENCES orders (order_id),
                FOREIGN KEY (product_id) REFERENCES products (product_id)
            )
        """)
        con.commit()
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

create_tables()

def add_user():
    try:
        user_id = int(input("Enter the ID: "))
        username = input("Enter the username: ")
        email = input("Enter the email: ")
        password = input("Enter the password: ")
        con.execute(
            "INSERT INTO users (id, username, email, password) VALUES (?, ?, ?, ?)",
            (user_id, username, email, password)
        )
        con.commit()
        print("User added successfully.")
    except sqlite3.IntegrityError:
        print("Error: User ID or username already exists.")
    except sqlite3.Error as e:
        print("Error adding user:", e)

def add_product():
    try:
        name = input("Enter the product name: ")
        description = input("Enter the product description: ")
        price = float(input("Enter the price: "))
        stock = int(input("Enter the stock quantity: "))
        con.execute(
            "INSERT INTO products (name, description, price, stock) VALUES (?, ?, ?, ?)",
            (name, description, price, stock)
        )
        con.commit()
        print("Product added successfully.")
    except sqlite3.Error as e:
        print("Error adding product:", e)

def place_order():
    try:
        user_id = int(input("Enter user ID: "))
        order_date = input("Enter order date (YYYY-MM-DD): ")
        con.execute(
            "INSERT INTO orders (user_id, order_date) VALUES (?, ?)",
            (user_id, order_date)
        )
        con.commit()
        order_id = con.execute("SELECT last_insert_rowid()").fetchone()[0]
        print(f"Order placed successfully with Order ID: {order_id}")
        
        while True:
            product_id = int(input("Enter product ID to add to order (0 to finish): "))
            if product_id == 0:
                break
            quantity = int(input("Enter quantity: "))
            con.execute(
                "INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
                (order_id, product_id, quantity)
            )
            con.commit()
            print("Product added to order.")
    except sqlite3.Error as e:
        print("Error placing order:", e)

def view_orders():
    try:
        orders = con.execute("SELECT * FROM orders").fetchall()
        if not orders:
            print("No orders found.")
            return
        for order in orders:
            print(f"Order ID: {order[0]}, User ID: {order[1]}, Order Date: {order[2]}")
            items = con.execute("SELECT * FROM order_items WHERE order_id = ?", (order[0],)).fetchall()
            for item in items:
                product = con.execute("SELECT name FROM products WHERE product_id = ?", (item[2],)).fetchone()
                print(f"  Product: {product[0]}, Quantity: {item[3]}")
    except sqlite3.Error as e:
        print("Error viewing orders:", e)

while True:
    print("\n1. Add User")
    print("2. Add Product")
    print("3. Place Order")
    print("4. View Orders")
    print("5. Exit")
    ch = input("Enter your choice: ")

    if ch == '1':
        add_user()
    elif ch == '2':
        add_product()
    elif ch == '3':
        place_order()
    elif ch == '4':
        view_orders()
    elif ch == '5':
        con.close()
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")

