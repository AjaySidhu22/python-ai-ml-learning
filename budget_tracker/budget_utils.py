# budget_utils.py
# Core logic for Personal Budget Tracker
# Phase 1 -> Week 1-2 -> Mini Project

import csv
import os
from datetime import datetime

# ---------- Constants ----------

CSV_FILE = "transactions.csv"

INCOME_CATEGORIES = ["Salary", "Freelance", "Investment", "Gift", "Other"]

EXPENSE_CATEGORIES = [
    "Food", "Rent", "Transport", "Utilities",
    "Healthcare", "Education", "Entertainment", "Other"
]

CSV_HEADERS = ["date", "type", "category", "amount", "description"]

# ---------- File Operations ----------

def initialize_file():
    """Create transaction.csv with headers if it does not exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)
            print(f"Created new file: {CSV_FILE}")


def load_transactions():
    """Load all transactions from CSV and return as list od dict."""
    initialize_file()
    transactions = []
    try:
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                transactions.append({
                    "date":        row["date"],
                    "type":        row["type"],
                    "category":    row["category"],
                    "amount":      float(row["amount"]),
                    "description": row["description"]
                })
    except FileNotFoundError:
        print("No trancation file found. Starting fresh.")
    return transactions


def save_transaction(transaction):
    """Append a single transaction dict to the CSV file."""
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
        writer.writerow(transaction)


# ---------- Input Validation ----------

def get_valid_amount():
    """Promt user for a positive number. Keep asking until valid."""
    while True:
        try:
            amount = float(input(" Enter amount: "))
            if amount <= 0:
                print("  Amount must be greater than zero. Try again.")
                continue
            return round(amount, 2)
        except ValueError:
            print("  Invalid input. Enter a number like 500 or 1250.75")


def get_valid_category(transaction_type):
    """Show category list and return valid selectio."""
    if transaction_type == "income":
        categories = INCOME_CATEGORIES
    else:
        categories = EXPENSE_CATEGORIES

    print(" Categories:")
    for i, cat in enumerate(categories, start=1):
        print(f" {i}. {cat}")

    while True:
        try:
            choice = int(input(f"  Choose category (1-{len(categories)}): "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print(f"  Enter a number between 1 and {len(categories)}")
        except ValueError:
            print("  Invalid input. Enter a number.")


# ---------- core Features ----------

def add_transaction(transaction_type):
    """Collect details from user and save a new transaction."""
    print(f"\n --- Add {transaction_type.capitalize()} ---")

    amount = get_valid_amount()
    category = get_valid_category(transaction_type)
    description = input("  Enter description: ").strip()
    if not description: 
        description = "No description"

    transaction = {
        "date":        datetime.now().strftime("%Y-%m-%d"),
        "type":        transaction_type,
        "category":    category,
        "amount":      amount,
        "description": description
    }

    save_transaction(transaction)
    print(f"\n  {transaction_type.capitalize()} of {amount:.2f} saved under '{category}'")

def view_all_transactions():
    """Print all transactions in a formatted table."""
    transactions = load_transactions() 

    if not transactions:
        print("\n No transactions found.")
        return 
    
    print("\n" + "=" *65)
    print(f"  {'DATE':<12} {'TYPE':<10} {'CATEGORY':<16} {'AMOUNT':>10} DESCRIPTION")
    print("=" * 65)

    for t in transactions:
        print(f"  {t['date']:<12} {t['type']:<10} {t['category']:<16} {t['amount']:>10.2f} {t['description']}")
    
    print("=" * 65)
    print(f"  Total transactions: {len(transactions)}")  


def check_balance():
    """Calculate and display current balance."""
    transactions = load_transactions()

    total_income  = sum(t["amount"] for t in transactions if t["type"]  == "income")
    total_expense = sum(t["amount"] for t in transactions if t["type"]  == "expense")
    balance       = total_income - total_expense

    print("\n" + "="*35)
    print("  CURRENT BALANCE")
    print("=" * 35)
    print(f"  Total Income:   {total_income:>10.2f}")
    print(f"  Total Expenses: {total_expense:>10.2f}")
    print("-" * 35)
    print(f"  Balance:        {balance:>10.2f}")
    print("=" * 35)

    if balance < 0:
        print("  WARNING: You are in deficit.")
    elif balance == 0:
        print("  balance is zero.")
    else:
        print("  You are in surplus.")
    

def monthly_report():
    """Show income and expense breakdown by category for current month."""
    transactions = load_transactions()
    current_month = datetime.now().strftime("%Y-%m")

    monthly = [t for t in transactions if t["date"].startswith(current_month)]

    if not monthly:
        print(f"\n  No transaction found for {current_month}")
        return
    
    income_by_category = {}
    expenses_by_category = {}

    for t in monthly:
        if t["type"] == "income":
            income_by_category[t["category"]] = (
                income_by_category.get(t["category"], 0) + t["amount"]
            )
        else:
            expenses_by_category[t["category"]] = (
                expenses_by_category.get(t["category"], 0) + t["amount"]
            )
    
    print(f"\n{'=' * 40}")
    print(f"  MONTHLY REPORT - {current_month}")
    print(f"{'=' * 40}")

    print("\n  INCOME:")
    if income_by_category:
        for cat, total in income_by_category.items():
            print(f"    {cat:<16} {total:>10.2f}")
    else:
        print("   No income this month.")

    print("\n EXPENSES:")
    if expenses_by_category:
        for cat, total in expenses_by_category.items():
            print(f"    {cat:<16} {total:>10.2f}")
    else:
        print("    NO expenses this month.")

    total_in  = sum(income_by_category.values())
    total_out = sum(expenses_by_category.values())

    print(f"\n  {'Total Income:':<20} {total_in:>10.2f}") 
    print(f"  {'Total Expenses:':<20} {total_out:>10.2f}")
    print(f"  {'Net this month:':<20} {total_in - total_out:>10.2f}")
    print("=" * 40)   