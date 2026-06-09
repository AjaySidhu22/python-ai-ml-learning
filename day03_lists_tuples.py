# Day 3 - Lists and Tuples
# Phase 1 -> Week 1 -> Day 3

# ---------- 1. Creating lists ----------
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14, None]
empty = []
nested = [[1, 2], [3, 4], [5, 6]]

print(numbers)
print(mixed)
print(empty)
print(nested)

# ---------- 2. Indexing and slicing ----------
scores = [95, 87, 92, 98, 90]
print(scores[0])    # first
print(scores[-1])   # last
print(scores[1:3])  # slice
print(scores[::-1]) # reversed

# ---------- 3. Lists are mutable ----------
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits[0] = "mango"   # change first item
print(fruits)         # mango replaces apple

# ---------- 4. List methods ----------
ml_topics = ["Python", "NumPy", "Pandas"]
print(ml_topics)

ml_topics.append("Matplotlib")    # add one item
print(ml_topics)

ml_topics.extend(["Scikit-learn", "PyTorch"])
print(ml_topics)

ml_topics.insert(1, "Statistics")  # insert at position 1
print(ml_topics)

ml_topics.remove("Statistics")      # remove by value
print(ml_topics)

popped = ml_topics.pop()            # removes and returns last item
print(f"Popped: {popped}")
print(ml_topics)

print(f"Length: {len(ml_topics)}")
print(f"Index of Pandas: {ml_topics.index("Pandas")}")
print(f"Count of Python: {ml_topics.count("Python")}")

# ---------- 5. Sorting ----------
nums = [5, 2, 8, 1, 9, 3]
nums.sort()     # sorts in place, ascending
print(nums)

nums.sort(reverse=True)   # descending
print(nums)

words = ["banana", "apple", "cherry", "date"]
words.sort()
print(words)               # alphabatical

# ---------- 6. Copy vs refrence - IMPORTANT ----------
original = [1, 2, 3, 4, 5]
reference = original      # NOT a copy - same list
copy = original.copy()    # real copy - seprate list

reference[0] = 999
print(f"Original after reference change: {original}")     # also chamged!
print(f"Copy after reference change: {copy}")              # unchanged

# ---------- 7. Nested lists - used in ML for matrices ----------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])   # first row
print(matrix[1][2])  # row 1, column 2 -> value 6
print(matrix[2][0])  # row 2, column 0 -> value 7

# ---------- 8. Tuples ----------
coordinates = (28.6, 77.2)   # Delhi coordinates
rgb = (255, 128, 0)      # orange color
image_shape = (224, 224, 3)   # ResNet input shape

print(coordinates)
print(rgb)
print(image_shape)
print(type(image_shape))      # <class 'tuple>

# access tuple items same as list
print(image_shape[0])   # 224
print(image_shape[-1])  # 3 (channels)

# tuples are immutable - this would cause error:
# image_shape[0] = 512  # TypeError

# tuple unpacking - very common in Python
height, width, channels = image_shape
print(f"Height: {height}, Width: {width}, Channels: {channels}")

# ---------- 9. Real AI/ML use case ----------
# Imagin these are model prediction scores
predictions = [0.92, 0.45, 0.88, 0.33, 0.76, 0.91]

predictions.sort(reverse=True)
print(f"Top prediction: {predictions[0]}")
print(f"Top 3 predictions: {predictions[:3]}")
print(f"Total predictions: {len(predictions)}")