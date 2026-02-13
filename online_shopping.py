clothes_store = {"Shirt": 25,"Jeans": 40,"Hoodie": 50,"Socks": 5,"Cap": 15}

cart = []

while True:
    print("\n---TRENDY THREADS CLOTHING---")
    print("1. View Collection")
    print("2. Add to Cart")
    print("3. View Cart and total")
    print("4. Remove item")
    print("5. Checkout & Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n---Our Collection---")
        for item, price in clothes_store.items():
            print(f".{item}: ${price}")

    elif choice == "2":
        print("\n---Add to Cart---")
        item = input("Enter the name of the clothing item: ").capitalize()
        if item in clothes_store:
            size = input(f"Enter size for the {item}? (S,M,L,XL): ").upper()
            cart.append({"name": item, "size": size, "price": clothes_store[item]})
            print(f"Added {size} {item} to your cart.")
        else:
            print("Sorry, we don't carry that item.")

    elif choice == "3":
        print("\n---YOUR SHOPPING BAG---")
        if not cart:
            print("Your Cart is empty.")
        else:
            total = 0
            for product in cart:
                print(f"- {product['size']} {product['name']}: ${product['price']}")
                total += product['price']
            print(f"\nGRAND TOTAL: ${total}")

    elif choice == "4":
        if not cart:
            print("Nothing to remove!")
        else:
            item_name = input("Enter item name to remove: ").capitalize()
            found = False

            for product in cart:
                if product['name'] == item_name:
                    cart.remove(product)
                    print(f"Removed {item_name} from cart.")
                    found = True
                    break

            if not found:
                print("Item not found in cart.")

    elif choice == "5":
        print("Thank you for Visiting! Your order is being processed.")
        break