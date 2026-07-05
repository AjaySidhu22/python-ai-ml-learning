# Day 9 - Exception Handling
# Phase 1 -> Week 1-2 -> Day 9

# ---------- 1. Basic try / except ----------
print("=== PART 1: Basic try / except ===")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    number = int("hello")
except ValueError:
    print("Cannot convert 'hello' to an integer")

try:
    items = [1, 2, 3]
    print(items[10])
except IndexError:
    print("Index does not exist in the list")

# ---------- 2. Catching the error message with `as e` ----------
print("\n=== PART 2: Capturing Error Details ===")

try:
    result = 10/0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError caught: {e}")

try:
    number = int("abc")
except ValueError as e:
    print(f"ValueError caught: {e}")

# ---------- 3. Multiple except blocks ----------
print("\n=== PART 3: Multiple except Blocks ===")

def parse_value(value):
    try:
        result = int(value)
        items = [10, 20, 30]
        return items[result]
    except ValueError:
        print(f" valueError: '{value}' is not a valid integer")
    except IndexError:
        print(f" IndexError: inddex {value} is out of range")

parse_value("hello")
parse_value("10")
parse_value("1")

# ---------- 4. else and finally ----------
print("\n=== PART 4. else and finally ===")

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f" Error: {e}")
    else:
        print(f" Success: {a} / {b} = {result}")
    finally:
        print(f" finally block always runs")
    
divide(10, 2)
divide(10, 0)

# ---------- 5. File handling with exceptions ----------
print("\n=== PART 5: File Exception Handling ===")

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print(f" File content: {content[:50]}")
    except FileNotFoundError:
        print(f" File '{filename} not found")
    
read_file("notes.txt")
read_file("does_not_exist.txt")

# ---------- 6. raise - intentionally raising exceptions ----------
print("\n=== PART 6: raise ===")

def set_learning_rate(lr):
    if not isinstance(lr, (int, float)):
        raise TypeError(f"Learning rate must be a number, got {type(lr)}")
    if lr <= 0:
        raise ValueError(f"Learning rate must be positive, got {lr}")
    if lr > 1:
        raise ValueError(f"Learning rate must be <= 1, got {lr}")
    print(f" Learning rate set to: {lr}")

try:
    set_learning_rate(0.01)
except (TypeError, ValueError) as e:
    print(f" Error: {e}")

try:
    set_learning_rate(-0.5)
except (TypeError, ValueError) as e:
    print(f" Error: {e}")
    
try:
    set_learning_rate("fast")
except (TypeError, ValueError) as e:
    print(f" Error: {e}")

# ---------- 7. Custom exceptions ----------
print("n=== PART 7: Custom Exceptions ===")

class InvalidDataError(Exception):
    pass

class ModelNotTrainedError(Exception):
    pass

def load_dataset(filepath):
    if not filepath.endswith(".csv"):
        raise InvalidDataError(f"Expected .csv file, got: {filepath}")
    print(f" Loading dataset from: {filepath}")

def predict(model_trained):
    if not model_trained:
        raise ModelNotTrainedError("Model must be trained before prediction")
    print(" Prediction complete")

try:
    load_dataset("data.json")
except InvalidDataError as e:
    print(f" InvalidDataError: {e}")

try:
    load_dataset("data.csv")
except InvalidDataError as e:
    print(f" InvalidDataError: {e}")

try:
    predict(False)
except ModelNotTrainedError as e:
    print(f" ModelNotTrainedError: {e}")

try:
    predict(True)
except ModelNotTrainedError as e:
    print(f" ModelNotTrainedError: {e}")

# ---------- 8. AI/ML use case - safe CSV row processing ----------
print("\n=== PART 8: AI/ML Use Cse - Safe Data Processing ===")

import csv

rows = [
    {"name": "Alice", "age": "25", "score": "88.5"},
    {"name": "Bob", "age": "abc", "score": "91.0"},
    {"name": "Carol", "age": "22", "score": "not_a_number"},
    {"name": "Dave", "age": "28", "score": "79.5"},
]

valid_rows = []
error_count = 0

for row in rows:
    try:
        age = int(row["age"])
        score = float(row["score"])
        valid_rows.append({"name": row["name"], "age": age, "score": score})
    except ValueError as e:
        print(f" Skipping row for {row['name']}: {e}")
        error_count += 1
    
print(f"\n Valid rows: {len(valid_rows)}")
print(f" Error skipped: {error_count}")
for r in valid_rows:
    print(f" {r}")