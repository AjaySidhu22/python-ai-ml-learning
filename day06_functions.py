# Day 6 - Functions 
# Phase 1 -> Week 1-> Day 6

# ---------- 1. Basic function ----------
def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

print(greet("Ajay"))
print(greet("Rahul"))

# ---------- 2. Function with multiple peremeters ----------
def add(a, b):
    """Returns sum of two numbers."""
    return a + b

print(add(10, 20))
print(add(3.14, 2.86))

# ---------- 3. Default parameters ----------
def greet_language(name, language="English"):
    """Greets in specified language."""
    if language == "Hindi":
        return f"Namaste, {name}!"
    elif language == "Punjabi":
        return f"Sat Sri Akal, {name}!"
    else:
        return f"Hello, {name}!"

print(greet_language("Ajay"))
print(greet_language("Ajay", "Hindi"))
print(greet_language("Ajay", "Punjabi"))

# ---------- 4. Multiple return values ----------
def get_stats(numbers):
    """Returns min, max and average of a list."""
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers)/ len(numbers)
    return minimum, maximum, average

scores = [85, 92, 78, 95, 88, 72, 91]
low, high, avg = get_stats(scores)
print(f"Min: {low}, Max: {high}, Avg: {avg:.2f}")

# ---------- 5. *args ----------
def total_marks(*args):
    """Calculates total of any number of marks."""
    print(f"Received marks: {args}")
    print(f"Type: {type(args)}")
    return sum(args)

print(total_marks(85, 92, 78))
print(total_marks(85, 92, 78, 95, 88))

# ---------- 6. **kwargs ----------
def show_model_config(**kwargs):
    """Display model configuration."""
    print("\nModel Configuration:")
    for key, value in kwargs.items():
        print(f" {key}: {value}")

show_model_config(model="ResNet50", learning_rate=0.001, batch_size=32, epochs=100)

# ---------- 7. Scope demonstration ----------
global_var = "I am global"

def scope_demo():
    local_var = "I am local"
    print(global_var)   # can access global inside functio
    print(local_var)    # local variable works inside

scope_demo()
print(global_var)  # works outside
# print(local_var)  # would cause NameError

# ---------- 8. Functions calling functions ----------
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenhite."""
    return (celsius * 9/5) + 32

def describe_temperature(celsius):
    """Describes temperature in human terms."""
    fahrenheit = celsius_to_fahrenheit(celsius)
    if celsius < 0:
        description = "Freezing"
    elif celsius < 15:
        description = "Cold"
    elif celsius < 25:
        description = "Pleasant"
    elif celsius < 35:
        description = "Warm"
    else:
        description = "Hot"
    return f"{celsius}°C = {fahrenheit:.1f}°F - {description}"

print(describe_temperature(-5))
print(describe_temperature(10))
print(describe_temperature(22))
print(describe_temperature(40))

# ---------- 9. Real AI/ML use case ----------
def preprocess_text(text):
    """
    Cleans and preprocesses text for NLP.
    Used in real AI pipelines before feeding to moddel.
    """
    text = text.strip()
    text = text.lower()
    text = text.replace("!", "")
    text= text.replace("?", "")
    text = text.replace(",", "")
    words = text.split()
    return words

def calculate_accuracy(predictions, actual):
    """
    Calculates model accuracy.
    predictions: list of predicted labels
    actual: list of true labels
    """
    correct = 0
    for pred, true in zip(predictions, actual):
        if pred == true:
            correct += 1
    accuracy = correct / len(actual)
    return accuracy

# test preprocess
raw_text = " Machine Learning is Amazing, and Powerful!"
processed = preprocess_text(raw_text)
print(f"\nOriginal: {raw_text}")
print(f"Processed: {processed}")

# test accuracy
predicted = [1, 0, 1, 1, 0, 1, 0, 0]
actual    = [1, 0, 1, 0, 0, 1, 1, 0]
acc = calculate_accuracy(predicted, actual)
print(f"\nModel Accuracy: {acc:.2%}")                          