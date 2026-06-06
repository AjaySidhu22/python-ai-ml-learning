# Day 1 - Variables and Data Types
# Type this entire file yourself

# --- Integers ---
age = 25
year = 2025
negative = -10
print(age)         # 25
print(type(age))   # <class 'int'>

# --- Floats ---
price = 99.99
pi = 3.14159
print(price)
print(type(price))

# --- Strings ---
name = "Rahul"
city = 'Varanasi'
greeting = f"Hello, my name is {name} and I live in {city}"
print(greeting)

# --- Booleans ---
is_student = True
is_working = False
print(is_student)
print(type(is_student))

# --- None (means "no value") ---
result = None
print(result)
print(type(result))

# --- Checking types ---
print(type(42))       # int
print(type(3.14))     # float
print(type("hello"))  # str
print(type(True))     # bool

# --- Type conversion ---
x = "100"        # this is a STRING "100"
y = int(x)       # now it's INTEGER 100
z = float(x)     # now it's FLOAT 100.0
print(y + 50)    # 150
print(z + 0.5)   # 100.5

# --- Basic math ---
a = 10
b = 3
print(a + b)   # 13  (addition)
print(a - b)   # 7   (subtraction)
print(a * b)   # 30  (multiplication)
print(a / b)   # 3.333...  (division - always float)
print(a // b)  # 3   (floor division - integer result)
print(a % b)   # 1   (modulo - remainder)
print(a ** b)  # 1000 (power: 10 to the power 3)