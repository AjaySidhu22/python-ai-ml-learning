# Day 19 - Generators and Iterators
# Phase 1 -> Week 3-4 -> Day 19

import sys

# ----------1. Iterator protocol manually ----------
print("=== PART 1: Iterator Protocol ===")

class CountUp:
    def __init__(self, start, stop):
        self.current = start
        self.stop     = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value         = self.current
        self.current += 1
        return value
    
counter = CountUp(1, 6)
for num in counter:
    print(f"  {num}", end=" ")
print()

# manually using next()
counter2 = CountUp(10, 13)
print(f"  next: {next(counter2)}")
print(f"  next: {next(counter2)}")
print(f"  next: {next(counter2)}")
try:
    print(next(counter2))
except StopIteration:
    print("  StopIteration raised - iterator exhausted")


# ---------- 2. Basic generator with yield ----------
print("\n=== PART 2: Basic Generator ===")

def count_up(start, stop):
    current = start
    while current < stop:
        yield current 
        current += 1

gen = count_up(1, 6)
print(f"  Generator object: {gen}")

for num in gen:
    print(f"  {num}", end=" ")
print()

# Generator is exhausted now
remaining = list(gen)
print(f"  After exhaustion: {remaining}")


# ---------- 3. yield with state - fibonacci ----------
print("\n=== PART 3: Fibonacci Generator ===")

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib_nums = list(fibonacci(100))
print(f"  Fibonacci below 100: {fib_nums}")

# Take only first 5
fib_gen = fibonacci(1000)
first_five = [next(fib_gen) for _ in range(5)]
print(f"  First 5 fibonacci: {first_five}")

# ---------- 4. Memory comparison ----------
print("\n=== PART 4: Memory - Llist vs Generator ===")

n = 100_000

list_version = [x ** 2 for x in range(n)]
gen_version  = (x ** 2 for x in range(n))

list_size = sys.getsizeof(list_version)
gen_size  = sys.getsizeof(gen_version)

print(f" List of {n} squares:      {list_size:,} bytes")
print(f" Generator of {n} squares: {list_size:,} bytes")
print(f"  Memory ratio: {list_size // gen_size}x more for list")


# ---------- 5. Generator expressions ----------
print("\n=== PART 5: Generator Expressions ===")

data = [3, -1, 7, -4, 2, 8, -6, 5, 1, -2]

# list comprehension - builds full list 
positives_list = [x for x in data if x > 0]

# generator expression - lazy
positives_gen = [x for x in data if x > 0]

print(f"  List: {positives_list}")
print(f"  Generator sum: {sum(positives_gen)}")

# Chained generator expressions
numbers = range(1, 11)
result = sum(x ** 2 for x in numbers if x % 2 == 0)
print(f"  Sum of squares of even numbers 1-10: {result}")


# ---------- 6. Practical generator - file reading ----------
print("\n=== PART 6: Practical Generator - Reading Files ===")

def read_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()

# Write a test file first
with open("sample_data.txt", "w", encoding="utf-8") as f:
    for i in range(1, 6):
        f.write(f"Row {i}: data point {i * 10}\n")

print("  Reading file line by line using generator:")
for line in read_lines("sample_data.txt"):
    print(f"  {line}")


# ---------- 7. AI/ML use case - batch generator ----------
print("\n=== PART 7: AI/ML Use Case - Batch Generator ===")

def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i : i + batch_size]

dataset = list(range(1, 21))   # 20 samples
batch_size = 4

print(f"  dataset: {dataset}")
print(f"  Batch size: {batch_size}")
print()

for batch_num, batch in enumerate(batch_generator(dataset, batch_size), start=1):
    print(f"  Batch {batch_num}: {batch}")


# ---------- 8. AI/ML use case - infinite data augmentation ----------
print("\n=== PART 8: AI/ML - Infinite Augmentation Generator ===")

import random

def augment_sample(sample):
    noise = random.uniform(-0.05, 0.05)
    return round(sample + noise, 4)

def infinite_augmented_stream(samples):
    while True:
        sample = random.choice(samples)
        yield augment_sample(sample)

base_samples = [0.5, 0.75, 0.25, 0.9, 0.1]
stream = infinite_augmented_stream(base_samples)

print("  10 augmented samples from infinite stream:")
for _ in range(10):
    print(f" {next(stream)}", end="  ")
print()