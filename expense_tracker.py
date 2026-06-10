import sys


def print_menu():
    print("\nExpense Tracker Menu")
    print("1. Add expense item")
    print("2. Remove expense item")
    print("3. Show current items")
    print("4. Finish and show totals")
    print("5. Exit without totals")


def get_price_input(prompt):
    while True:
        price_text = input(prompt).strip()
        try:
            price = float(price_text)
            if price < 0:
                raise ValueError
            return price
        except ValueError:
            print("Please enter a valid non-negative number for the price.")


def show_items(items):
    if not items:
        print("No expense items recorded yet.")
        return
    print("\nCurrent expense items:")
    for index, (name, price) in enumerate(items, start=1):
        print(f"{index}. {name} - ${price:.2f}")
    print(f"Total items: {len(items)}")


def remove_item(items):
    if not items:
        print("No items available to remove.")
        return
    show_items(items)
    while True:
        choice = input("Enter the number of the item to remove (or press Enter to cancel): ").strip()
        if choice == "":
            print("Remove cancelled.")
            return
        if choice.isdigit():
            index = int(choice)
            if 1 <= index <= len(items):
                item = items.pop(index - 1)
                print(f"Removed '{item[0]}' priced at ${item[1]:.2f}.")
                return
        print("Please enter a valid item number.")


def show_summary(items):
    monthly_total = sum(price for _, price in items)
    quarterly_total = monthly_total * 3
    yearly_total = monthly_total * 12

    print("\nExpense summary for the month:")
    show_items(items)
    print(f"\nMonthly expense total: ${monthly_total:.2f}")
    print(f"Quarterly expense total: ${quarterly_total:.2f}")
    print(f"Yearly expense total: ${yearly_total:.2f}")


def main():
    print("Welcome to the simple command-line Expense Tracker!")
    items = []

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter item name: ").strip()
            if not name:
                print("Item name cannot be empty.")
                continue
            price = get_price_input("Enter item price: ")
            items.append((name, price))
            print(f"Added '{name}' with price ${price:.2f}.")

        elif choice == "2":
            remove_item(items)

        elif choice == "3":
            show_items(items)

        elif choice == "4":
            show_summary(items)
            print("\nThanks for using the Expense Tracker.")
            break

        elif choice == "5":
            print("Exiting without displaying totals. Goodbye.")
            break

        else:
            print("Please choose a valid option between 1 and 5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Exiting Expense Tracker.")
        sys.exit(0)
