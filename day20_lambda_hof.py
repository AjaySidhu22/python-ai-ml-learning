# Day 20 - Lambda and Higher-Order Functions
# Phase 1 -> Week 3-4 -> Day 20

from functools import reduce

# ---------- 1. Lambda basics ----------
print("=== PART 1: Lambda Basics ===")

square    = lambda x: x ** 2
add       = lambda x, y: x + y
is_even   = lambda x: x % 2 == 0
clamp     = lambda x, lo, hi: max(lo, min(hi, x))

print(f"  square(7)       = {square(7)}")
print(f"  add(3, 4)       = {add(3, 4)}")
print(f"  is_even(8)      = {is_even(8)}")
print(f"  is_even(7)      = {is_even(7)}")
print(f"  clamp(15, 0, 10)= {clamp(15, 0, 10)}")
print(f"  clamp(-3, 0, 10)= {clamp(-3, 0, 10)}")
print(f"  clamp(5, 0, 10) = {clamp(5, 0, 10)}")


# ---------- 2. map() ----------
print("\n=== PART 2: map() ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]

squared  = list(map(lambda x: x ** 2, numbers))
doubled = list(map(lambda x: x * 2, numbers))
as_floats = list(map(float, numbers))

print(f"  original: {numbers}")
print(f"  squared:  {squared}")
print(f"  doubled:  {doubled}")
print(f"  floats:   {as_floats}")

# map with strings - comman in data preprocessing
names = ["  alice ", " BOB ", " Charlie"]
cleaned = list(map(lambda s: s.strip().title(), names))
print(f"\n  raw names:     {names}")
print(f"  cleaned names: {cleaned}")

# map over two lists simultaneouslt
prices = [100, 200, 300, 400]
tax_rates = [0.05, 0.10, 0.15, 0.18]
final_prices = list(map(lambda p, t: round(p * (1 + t), 2), prices, tax_rates))
print(f"\n prices:       {prices}")
print(f"  tax rates:   {tax_rates}")
print(f"  final prices: {final_prices}")


# ---------- 3. filter() ----------
print("\n=== PART 3: filter() ===")

scores = [45, 88, 23, 91, 67, 55, 78, 95, 12, 82]

passed  = list(filter(lambda x: x >= 60, scores))
failed  = list(filter(lambda x: x < 60, scores))
high    = list(filter(lambda x: x >= 85, scores))

print(f"  all scores: {scores}")
print(f"  passed (>=60): {passed}")
print(f"  failed (<60):  {failed}")
print(f" high (>=85):  {high}")

# filter with strings
words = ["apple", "ai", "banana", "ml", "cherry", "deep", "learning"]
long_words  = list(filter(lambda w: len(w) > 4, words))
short_words = list(filter(lambda w: len(w) <= 2, words))
print(f"\n words:      {words}")
print(f"  long (>4):   {long_words}")
print(f"  short (<=2): {short_words}")


# ---------- 4. reduce() ----------
print("\n=== PART 4: reduce() ===")

numbers = [1, 2, 3, 4, 5]

total   = reduce(lambda a, b: a + b, numbers)
product = reduce(lambda a, b: a * b, numbers)
maximum = reduce(lambda a, b: a if a > b else b, numbers)

print(f"  numbers: {numbers}")
print(f"  sum:     {total}")
print(f"  pproduct: {product}")
print(f"  maximum: {maximum}")

# reduce to build a string
words = ["python", "is", "great", "for", "AI"]
sentence = reduce(lambda a, b: a + " " + b, words)
print(f"\n  words:    {words}")
print(f"  sentence: {sentence}")


# ---------- 5. sorted() with key ----------
print("\n PART 5: sorted() with key ===")

students = [
    {"name": "Alice",   "grade": 88, "age": 22},
    {"name": "Bob",     "grade": 95, "age": 20},
    {"name": "Charlie", "grade": 72, "age": 23},
    {"name": "Diana",   "grade": 95, "age": 21},
    {"name": "Eve",     "grade": 67, "age": 22},
]

by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
by_name  = sorted(students, key=lambda s: s["name"])
by_grade_then_age = sorted(
    students,
    key=lambda s: (-s["grade"], s["age"])
)

print("  By grade (highest first):")
for s in by_grade:
    print(f"    {s['name']:<10} grade={s['grade']}  age={s['age']}")

print("\n  By name (alphabetical):")
for s in by_name:
    print(f"     {s['name']:<10} grade={s['grade']}")

print("\n  By grade desc then age asc:")
for s in by_grade_then_age:
    print(f"    {s['name']:<10} grade={s['grade']}  age={s['age']}")


# ---------- 6. AI/ML use case - combining all together ----------
print("\n=== PART 6: AI/ML Pipeline with map/filter/reduce ===")

raw_predictions = [
    {"lable": "cat",  "confidence": 0.92},
    {"lable": "dog",  "confidence": 0.45},
    {"lable": "bird", "confidence": 0.88},
    {"lable": "fish", "confidence": 0.31},
    {"lable": "cat",  "confidence": 0.76},
    {"lable": "dog",  "confidence": 0.95},
]

# Step 1 - filter low confidence predictions
high_conf = list(filter(
    lambda p: p["confidence"] >= 0.7, 
    raw_predictions
))

# Step 2 - extract just confidence scores
conf_scores = list(map(lambda p: p["confidence"], high_conf))

# Step 3 - compute average confidence using reduce
avg_conf = reduce(lambda a, b: a + b, conf_scores) / len(conf_scores)

# Steps 4 - sort by confideb=nce descending
ranked = sorted(high_conf, key=lambda p: p["confidence"], reverse=True)

print(f"  Total predictions:      {len(raw_predictions)}")
print(f"  High confidence (>=0.7): {len(high_conf)}")
print(f"  Average confidence:     {avg_conf:.4f}")
print(f"\n  Ranked predictions:")
for p in ranked:
    print(f"    {p['lable']:<6} - {p['confidence']:.2f}")
