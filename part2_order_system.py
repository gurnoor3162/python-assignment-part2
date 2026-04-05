def show_menu():
    print("\n--- MENU ---")
    print("1. Pizza - 200")
    print("2. Burger - 100")
    print("3. Pasta - 150")
    print("4. Exit")


def main():
    order = []
    prices = {
        "Pizza": 200,
        "Burger": 100,
        "Pasta": 150
    }

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            order.append("Pizza")
            print("Pizza added")
        elif choice == "2":
            order.append("Burger")
            print("Burger added")
        elif choice == "3":
            order.append("Pasta")
            print("Pasta added")
        elif choice == "4":
            break
        else:
            print("Invalid choice")

    total = 0
    print("\n--- Your Order ---")
    
    for item in order:
        print(item, "-", prices[item])
        total += prices[item]

    print("Total Amount:", total)


if __name__ == "__main__":
    main()
