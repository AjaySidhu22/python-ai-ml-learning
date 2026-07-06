# Personal Budget Tracker CLI

A command-line budget tracking application built in Python.
This is the Week 1-2 mini project from my Python → AI/ML learning roadmap.

## What It Does

- Add income and expense transactions
- Categorize each transaction
- View all transactions in a formatted table
- View monthly income and expense breakdown by category
- Check current balance at any time
- All data persists between sessions using CSV file storage

## How to Run

```powershell
# Navigate to project folder
cd E:\PythonLearning\phase1_foundations\budget_tracker

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run the application
python main.py
```

## Project Structure

budget_tracker/
├── main.py            # Entry point — menu loop and user interaction
├── budget_utils.py    # Core logic — all functions for data handling
├── transactions.csv   # Auto-created — stores all transaction data
└── README.md          # This file

## Concepts Demonstrated

| Concept | Where Used |
|---|---|
| Variables and Data Types | Transaction amounts, dates, categories |
| Strings and f-strings | Formatted reports and user messages |
| Lists and Dictionaries | Storing and grouping transactions |
| Control Flow | Menu navigation and input validation |
| Functions | Each feature isolated in its own function |
| List Comprehensions | Filtering transactions by month and type |
| File I/O | Loading and saving CSV data |
| Exception Handling | Invalid input protection throughout |
| Modules | csv, os, datetime, custom budget_utils |

## Sample Output

========================================
PERSONAL BUDGET TRACKER

Add Income
Add Expense
View All Transactions
View Monthly Report
Check Balance
Exit
========================================

MONTHLY REPORT — 2026-07
INCOME:
Salary           3000000.00
Freelance        2500000.00
EXPENSES:
Food               20000.00
Utilities          40000.00
Education         150000.00
Net this month:    5290000.00