# Day 5 - Control Flow
# Phase 1 -> Week 1 -> Day 5

# ---------- 1. Baswic if/elif/else ----------
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print(" Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# ---------- 2. Logical operators ----------
age = 22
has_degree = True

if age >= 18 and has_degree:
    print("Eligible for job application")

salary = 80000
experience = 3

if salary > 100000 or experience > 5:
    print("Senior candidate")
else:
    print("Junior candidate")

is_weekend = False
if not is_weekend:
    print("It is a weekday - study Python!")

# ---------- 3. for loop with list ----------
ml_topics = ["Python", "NumPy", "Pandas", "PyTorch", "LangChain"]

for topic in ml_topics:
    print(f"Learning: {topic}")

# ---------- 4. for loop with range ----------
print("\nCounting with range:")
for i in range(1, 6):
    print(f"Step {i}")

# ---------- 5. enumerate ----------
print("\nWith index:")
for index, topic in enumerate(ml_topics):
    print(f"{index}: {topic}")

# ---------- 6. for loop with dictonary ----------
model_scores = {
    "Linear Regression": 0.82,
    "Random Forest": 0.91,
    "XGBoost": 0.94,
    "Neural Network": 0.96
}

print("\nModel Scores:")
for model, score in model_scores.items():
    if score >= 0.90:
        print(f"{model}: {score} <- GOOD MODEL")
    else:
        print(f"{model}: {score}")

# ---------- 7. while loop ----------
print("\nWhile loop:")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1 # count = count +1

print("Loop finished")

# ---------- 8. break ----------
print("\nBreak example:")
for i in range(10):
    if i == 5:
        print("Found 5 - stopping!")
        break
    print(i)

# ---------- 9. continue ----------
print("\nContinue example - odd numbers only:")
for i in range(1, 11):
    if i % 2 == 0:
        continue     # skip even numbers
    print(i)

# ---------- 10. Nested loops ----------
print("\nMultiplication table 1-3:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")

# ---------- 11. Real AI/ML use case ----------
# Simulate finding best model threshold 
predictions = [0.92, 0.45, 0.88, 0.33, 0.76, 0.91, 0.55, 0.67]
threshold = 0.80

print(f"\nPredictions above threshold {threshold}:")
high_confidence = []

for i, pred in enumerate(predictions):
    if pred >= threshold:
        high_confidence.append(pred)
        print(f" Sample {i}: {pred} -> POSITIVE")
    else:
        print(f" Sample {i}: {pred} -> NEGATIVE")

print(f"\nHigh confidence predictions: {high_confidence}")
print(f"Total positive: {len(high_confidence)}")
print(f"Total negative: {len(predictions) - len(high_confidence)}")