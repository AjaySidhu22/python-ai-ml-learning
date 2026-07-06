# main.py
# Entry Point for Personal Budget Tracker CLI
# Phase 1 -> Week 1-2 -> Mini Project

import budget_utils


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("     PERSONAL BUDGET TRACKER")
    print("=" * 40)
    print("  1. Add Income")
    print("  2. Add Expenses")
    print("  3. View All Transactions")
    print("  4. View Monthly Report")
    print("  5. Check Balance")
    print("  6. Exit")
    print("=" * 40)

def get_menu_choice():
    """Get a valid manu choice from the user."""
    while True:
        try:
            choice = int(input("  Enter choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("  Please enter a number between 1 and 6.")
        except ValueError:
            print("  Invalid input. Enter a number.")


def main():
    """Main application loop."""
    print("\nWelcome to Personal Budget Tracker!")
    budget_utils.initialize_file()

    while True:
        print_menu()
        choice = get_menu_choice()

        if choice == 1:
            budget_utils.add_transaction("income")

        elif choice == 2:
            budget_utils.add_transaction("expense")
        
        elif choice == 3:
            budget_utils.view_all_transactions()

        elif choice == 4:
            budget_utils.monthly_report()

        elif choice == 5:
            budget_utils.check_balance()
        
        elif choice == 6:
            print("\nGoodbye. Your data has been saved.")
            break


if __name__ == "__main__":
    main()