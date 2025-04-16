from dao.order_processor import OrderProcessor
from entity.user import User
from entity.electronics import Electronics
from entity.clothing import Clothing

def main():
    processor = OrderProcessor()

    while True:
        print("\nMenu:")
        print("1. Create User")
        print("2. Create Product")
        print("3. Create Order")
        print("4. Cancel Order")
        print("5. Get All Products")
        print("6. Get Order by User")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            try:
                user_id = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = input("Enter Role (Admin/User): ")
                user = User(user_id, username, password, role)
                success = processor.create_user(user)
                if success:
                    print("✅ User created successfully.")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            try:
                admin_id = int(input("Enter Admin User ID: "))
                username = input("Enter Admin Username: ")
                password = input("Enter Admin Password: ")
                role = "Admin"
                admin_user = User(admin_id, username, password, role)

                product_id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                desc = input("Enter Description: ")
                price = float(input("Enter Price: "))
                stock = int(input("Enter Quantity In Stock: "))
                type_ = input("Enter Type (Electronics/Clothing): ")

                if type_.lower() == 'electronics':
                    brand = input("Enter Brand: ")
                    warranty = int(input("Enter Warranty Period (months): "))
                    product = Electronics(product_id, name, desc, price, stock, brand, warranty)
                elif type_.lower() == 'clothing':
                    size = input("Enter Size: ")
                    color = input("Enter Color: ")
                    product = Clothing(product_id, name, desc, price, stock, size, color)
                else:
                    print("Invalid product type.")
                    continue

                processor.create_product(admin_user, product)
                print("✅ Product created successfully.")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                user_id = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = "User"
                user = User(user_id, username, password, role)

                num_items = int(input("How many products to order? "))
                products = []

                for i in range(num_items):
                    product_id = int(input(f"Enter Product ID #{i+1}: "))
                    # Create dummy Product just with product_id (only needed for ID)
                    product = Electronics(product_id, "", "", 0.0, 0, "", 0)  # type doesn't matter here
                    products.append(product)

                processor.create_order(user, products)
                print("✅ Order created successfully.")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            try:
                user_id = int(input("Enter User ID: "))
                order_id = int(input("Enter Order ID: "))
                processor.cancel_order(user_id, order_id)
                print("order cancelled successfully!.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            try:
                products = processor.get_all_products()
                for row in products:
                    print(row)
                print("successfully got all products.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '6':
            try:
                user_id = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = "User"
                user = User(user_id, username, password, role)

                orders = processor.get_order_by_user(user)
                for order in orders:
                    print(order)
                # print("✅ successfully got order by user.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

