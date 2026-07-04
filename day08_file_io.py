# Day 8 - File I\O
# Phase 1 -> Week 1-2 -> Day 8

import csv
import os

# ---------- 1. Writing a text file ----------
print("=== PART 1: Writing a Text file ===")

with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Line 1: Python is powerful\n")
    f.write("Line 2: File I/O is essential for AI\n")
    f.write("Line 3: Always use the with statement\n")

print("notes.txt has been written.")

# ---------- 2. Reading Entire File at once ----------
print("\n=== PART 2. Reading Entire File ===")

with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)

# ---------- 3. Reading line by line ----------
print("=== PART 3: Reading Line by Line ===")

with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # strip() removes the \n at end of each line

# ---------- 4. Reading into a list ----------
print("\n=== PART 4: readlines() into a List ===")

with open("notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
print(f"First line: {lines[0].strip()}")
print(f"Last line: {lines[-1].strip()}")

# ---------- 5. Appending to a file ----------
print("\n=== PART 5: Appending to File ===")

with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Line 4: Append later - data persists!\n")

print("Line appended . Reading again:")

with open("notes.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ---------- 6. Writing a CSV file ----------
print("=== PART 6: Writing a CSV File ===")

students = [
    ["name", "age", "score"],
    ["Ajay", 21, 92.5],
    ["Priya", 22, 88.0],
    ["Rahul", 20, 95.5],
    ["Anita", 23, 79.0],
]

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)

print("students.csv has been written.")

# ---------- 7. Reading a CSV file ----------
print("\n=== PART 7: Reading a CSV File ===")

with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ---------- 8. Reading CSV into list of dicts (more useful) ----------
print("\n=== PART 8: CSV as Dictionaries ===")

with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    students_data = list(reader)

for student in students_data:
    print(f"Name: {student['name']}, Score: {student['score']}")

# ---------- 9. AI/ML use case - saving and loading results ----------
print("\n=== PART 9: AI/ML Use case - Saving Model Results ===")

# Simulate saving model accuracy results to a log file
results = [
    {"epoch": 1, "loss": 0.9234, "accuracy": 0.6112},
    {"epoch": 2, "loss": 0.7891, "accuracy": 0.7245},
    {"epoch": 3, "loss": 0.5432, "accuracy": 0.8301},
    {"epoch": 4, "loss": 0.3210, "accuracy": 0.9012},
    {"epoch": 5, "loss": 0.2100, "accuracy": 0.9456},
]

with open("training_log.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["epoch", "loss", "accuracy"])
    writer.writeheader()
    writer.writerows(results)

print("Training log saved.")

# Now read it back and find best epoch
with open("training_log.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    all_results = list(reader)

best = max(all_results, key=lambda row: float(row["accuracy"]))
print(f"Best epoch: {best['epoch']} with accuracy: {best['accuracy']}")

# ---------- 10. Check if file exists before reading ----------
print("\n=== PART 10: checking File Existance ===")

files_to_check = ["notes.txt", "students.csv", "training_log.csv", "missing.txt"]

for filename in files_to_check:
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"{filename} exists - size: {size} bytes")
    else:
        print(f"{filename} does NOT exist")