# Day 18 - Decorators
# Phase 1 -> Week 3-4 -> Day 18 

from functools import wraps
import time

# ---------- 1. Closure foundation ----------
print("=== PART 1: Closures ===")

def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)
times10 = multiplier(10)

print(f"double(5)  = {double(5)}")
print(f"triple(5)  = {triple(5)}")
print(f"times10(5) = {times10(5)}")

# ---------- 2. Building a decorator from scratch ----------
print("\n=== PART 2: First Decorator ===")

def simple_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  Finished: {func.__name__}")
        return result
    return wrapper
@simple_logger
def add(a, b):
    return a + b

@simple_logger
def greet(name):
    return f"Hello, {name}"

result1 = add(3, 4)
print(f"  Result: {result1}")

result2 = greet("Ajay")
print(f"  Result: {result2}")

# ---------- 3. Timer decorator - used constantly in AI/ML ----------
print("\n=== PART 3: Timer Decorator ===")

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = (end - start) * 1000
        print(f"  [{func.__name__}] took {elapsed:.2f}ms")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

@timer
def simulate_training(epochs):
    total_loss = 0.0
    for epoch in range(epochs):
        total_loss += 1 / (epoch + 1)
    return total_loss

result = slow_sum(1_000_000)
print(f" sum result: {result}")

loss = simulate_training(100)
print(f"  final loss: {loss:.4f}")


# ---------- 4. Decorator with arguments ----------
print("\n=== PART 4: Decorator with Arguments ===")

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(times):
                print(f"  Run {i + 1}/{times}:")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def train_epoch(epoch_num):
    loss = 1.0 / (epoch_num + 1)
    print(f"   epoch {epoch_num} loss: {loss:.4f}")
    return loss

train_epoch(1)


# ---------- 5. Stacking decorators ----------
print("\n=== PART 5: Stacking Decorators ===")

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f" LOG: calling {func.__name__} with args={args}")
        result = func(*args, **kwargs)
        print(f"  LOG: {func.__name__} returned {result}")
        return result
    return wrapper

@timer
@logger
def multiply(a, b):
    return a * b

multiply(6, 7)


# ---------- 6. Validator decorator - AI/ML input checking ----------
print("\n=== PART 6: Validator Decorator ===")

def validate_inputs(func):
    @wraps(func)
    def wrapper(data, *args, **kwargs):
        if not isinstance(data, list):
            raise TypeError(f"Expected list, got {type(data).__name__}")
        if len(data) == 0:
            raise ValueError("Data cannot be empty")
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("All values must be numeric")
        return func(data, *args, **kwargs)
    return wrapper

@validate_inputs
def compute_mean(data):
    return sum(data) / len(data)

@validate_inputs
def compute_std(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data) 
    return variance ** 0.5

print(f"  mean: {compute_mean([10, 20, 30, 40, 50]):.2f}")
print(f"  std:  {compute_std([10, 20, 30, 40, 50]):.2f}")

for bad_input in [{"key": 1}, [], [1, 2, "three"]]:
    try:
        compute_mean(bad_input)
    except (TypeError, ValueError) as e:
        print(f"  Error for {bad_input}: {e}")

    
# ---------- 7. @wraps importance ----------
print("\n=== PART 7: Why @wraps Matters ===")

def without_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@without_wraps
def function_a():
    """This is function A's docstring."""
    pass

@with_wraps
def function_b():
    """This is function B's docstring."""
    pass

print(f"  without @wraps - name: {function_a.__name__!r}")
print(f"  without @wraps - doc:  {function_a.__doc__!r}")
print(f"  with @wraps - name:    {function_b.__name__!r}")
print(f"  with @wraps - doc:     {function_b.__doc__!r}")