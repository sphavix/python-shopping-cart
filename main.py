def display_cart(cart):
    if not cart:
        print("cart is empty")
    else:
        print("Shopping cart:")

    total_price = 0
    for item in cart:
        print(f"{item['name']}: R{item['price']}")
        total_price += item['price']
    print(f"Total: R{total_price:.2f}")

def main():
    cart = []
    while True:
        print("\nShopping Cart App")
        print("1. Add Item to Cart")
        print("2. View Cart")
        print("3. Remove Item from cart")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            item = {"name": item_name, "price": item_price}
            cart.append(item)
            print('Item added to cart!')
        elif choice == '2':
            display_cart(cart)
        elif choice == '3':
            if not cart:
                print("Your cart is already empty")
            else:
                display_cart(cart)
                item_index = int(input("Enter the item number to remove: ")) -1
                if 0 <= item_index < len(cart):
                    removed_item = cart.pop(item_index)
                    print(f"{removed_item['name']} has been removed from the cart!")
                else:
                    print("Invalid item to remove")
        elif choice == '4':
            print("Exit the application")
        else:
            print("You have selected an invalid choice")

if __name__ == "__main__":
    main()
