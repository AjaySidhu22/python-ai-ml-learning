# Day 10 - Modules and Packages 
# Phase 1 -> Week 1-2 -> Day 10

# ---------- 1. Importing standard library modules ----------
print("=== PART 1: Standard Library Imports ===")

import math
import random
import os
import sys

print(f"math.pi = {math.pi}")
print(f"math.sqrt(144) = {math.sqrt(144)}")
print(f"math.floor(3.9) = {math.floor(3.9)}")
print(f"math.ceil(3.1) = {math.ceil(3.1)}")
print(f"randam.randint(1, 100) = {random.randint(1, 100)}")
print(f"os.getcwd() = {os.getcwd()}")
print(f"Python version = {sys.version}")

# ---------- 2. from ... import ----------
print("\n=== PART 2: from ... import ===")

from math import sqrt, pi, factorial
from random import choice, shuffle

print(f"sqrt(256) = {sqrt(256)}")
print(f"pi = {pi}")
print(f"factorial(6) = {factorial(6)}")

models = ["LinearRegression", "RandomForest", "XGBoost", "SVM"]
print(f"Random model chosen: {choice(models)}")

shuffle(models)
print(f"Shuffled models: {models}")

# ---------- 3. import with alias ----------
print("\n=== PART 3: import as alias ===")

import os.path as osp
import random as rnd

print(f"File exists: {osp.exists('notes.txt')}")
print(f"Random float: {rnd.uniform(0.0, 1.0):.4f}")

# ---------- 4. Exploring a module with dir() ----------
print("\n=== PART 4: Exploring a module ===")

math_items = [item for item in dir(math) if not item.startswith("_")]
print(f"math module contains {len(math_items)} public items")
print(f"First 10: {math_items[:10]}")

# ---------- 5. The detetime module ----------
print("\n=== PART 5: datetime Module ===")

from datetime import datetime, timedelta

now = datetime.now()
print(f"Current time: {now}")
print(f"Formated: {now.strftime('%Y-%m-%d %H:%M:%S')}")

tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

one_week_ago = now - timedelta(weeks=1)
print(f"One week ago: {one_week_ago.strftime('%Y-%m-%d')}")

# ---------- 6. Creating your own module ----------
print("\n=== PART 6: Creating Your Own Module ===")
print("Creating ml_utils.py...")

#  We will write the module content to a file 
module_code = '''# ml_utils.py - a utility module for ML tasks
def normalize(values):
    """Min-max normalize a list of numbers to range [0, 1]."""
    min_val = min(values)
    max_val = max(values)
    if max_val == min_val:
        return [0.0 for _ in values]
    return [(v - min_val) / (max_val - min_val) for v in values]

def calculate_accuracy(predictions, labels):
    """Calculate classification accuracy."""
    if len(predictions) != len(labels):
        raise ValueError("predictions and labels must have same length")
    correct = sum(p == l for p, l in zip(predictions, labels))
    return correct / len(labels)

def train_test_split(data, test_ratio=0.2):
    """Split data into train and test sets."""
    split_index = int(len(data) * (1 - test_ratio))
    return data[:split_index], data[split_index:]

ML_VERSION = "1.0.0"
'''

with open("ml_utils.py", "w", encoding="utf-8") as f:
    f.write(module_code)

print("ml_utils.py created.")

# ---------- 7. Importing and using your own module ----------
print("\n=== PART 7: Using Your Own Module ===")

import ml_utils

scores = [45, 92, 78, 55, 88, 100, 33, 67]
normalized = ml_utils.normalize(scores)
print(f"Original scores: {scores}")
print(f"Normalized: {[round(n, 3) for n in normalized]}")

predictions = [1, 0, 1, 1, 0]
labels = [1, 0, 0, 1, 0]
accuracy = ml_utils.calculate_accuracy(predictions, labels)
print(f"Accuracy: {accuracy:.2%}")

data = list(range(100))
train, test = ml_utils.train_test_split(data, test_ratio=0.2)
print(f"Train size: {len(train)}, Test size: {len(test)}")
print(f"Module version: {ml_utils.ML_VERSION}")

# ---------- 8. from your module import specific items ----------
print("\n=== PART 8: from ml_utils import ===")

from ml_utils import normalize, calculate_accuracy

data2 = [10, 20, 30, 40, 50]
print(f"Normalized: {normalize(data2)}")

# ---------- 9. pip and installed packages ----------
print("\n=== PART 9: Checking Installed Packages ===")

import subprocess
result = subprocess.run(
    ["pip", "list"],
    capture_output=True,
    text=True
)
lines = result.stdout.strip().split("\n")
print(f"Total packages installed: {len(lines) - 2 }")
print("First 8 packages:")
for line in lines[2:10]:
    print(f" {line}")

# ----------10. AI/ML relevance summary ----------
print("\n=== PART 10: AI/ML Sgandard Imports Preview ===")

print("The following are the most important imports you will use in every AI/ML project:")
print("  import numpy as np         # arrays, math, linear algebra")
print("  import pandas as pd        # dataframes, CSV loading")
print("  import matplotlib.pyplot as plt  # plotting")
print("  from sklearn.linear_model import LinearRegression  # ML model")
print(" import torch                # deep learning")
print("  from datetime import datetime  # standard utility modules")
print("\nYou have now built the foundation to use all of these.")