# Day 4 - Dictionaries and Sets
# Phase 1 Week 1 -> Day 4

# ---------- 1. Creating dictionaries

empty = {}
student = {
    "name": "Ajay",
    "age":  22,
    "city": "Hisar",
    "is_student": True
}
print(student)
print(type(student))

# ---------- 2. Accessing values ----------
print(student["name"])          # direct access
print(student["age"])
print(student.get("city"))      # safe access
print(student.get("phone"))     # key missing -> None
print(student.get("phone", "N/A"))  # key missing -> "N/A"

# ---------- 3. Adding and updating ----------
student["course"] = "AI/ML"     # add new key 
student["age"]   = 23      # updating existing key
print(student)

# ---------- 4. Dictionary methods ----------
print(student.keys())     # all keys
print(student.values())   # all values
print(student.items())    # all key-value pairs

# check if key exists
print("name" in student)  # True
print("phone" in student) # False

# removee a key 
removed = student.pop("is_student")
print(f"Removed: {removed}")
print(student)

# ---------- 5. Looping through dictionary ----------
ml_scores = {
    "Python": 95,
    "NumPy": 88,
    "Pandas": 82,
    "PyTorch": 75
}

for subject, score in ml_scores.items():
    print(f"{subject}: {score}")

# ---------- 6. Nested dictionary ----------
model_config = {
    "model_name": "ResNet50",
    "hyperparameters": {
        "learning_rate": 0.001,
        "batch_size": 32,
        "epochs": 100
    },
    "input_shape": (224, 224, 3)
}

print((model_config["model_name"]))
print(model_config["hyperparameters"]["learning_rate"])
print(model_config["hyperparameters"]["batch_size"])
print(model_config["input_shape"])

# ---------- 7. Dictionary comprehension ----------
# create a dict of squares
squeares = {x: x**2 for x in range(1, 6)}
print(squeares)

# filter scores above 80
high_scores = {k: v for k, v in ml_scores.items() if v > 80}
print(high_scores)

# ---------- 8. Sets ----------
fruits = {"apple", "banana", "cherry", "apple", "banana"}
print(fruits)       # duplicates removed automatically
print(type(fruits))

# empty set - must use set(), not {}
empty_set = set()
print(type(empty_set))

# add and remove
fruits.add("mango")
print(fruits)
fruits.discard("banana")   # remove - no error if missing
print(fruits)

# ---------- 9. Set operations ----------
ml_skills = {"Python", "NumPy", "Pandas", "PyTorch"}
ds_skills = {"Python", "Pandas", "Matplotlib", "SQL"}

print(ml_skills | ds_skills)   # union - all skills
print(ml_skills & ds_skills)   # intersection - comman skills
print(ml_skills - ds_skills)   # difference - only in ml_skills

# membership check - very fast
print("Python" in ml_skills)  # True
print("Java" in ml_skills)    # False

# ---------- 10. Real AI/ML use cases
# Count word frequency - used in NLP
sentence = "the cat sat on the mat the cat"
words = sentence.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

# unique words using set
unique_words =set(words)
print(f"Unique words: {unique_words}")
print(f"Vocabulary size: {len(unique_words)}")
