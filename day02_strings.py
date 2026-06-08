# Day 2 - Strings and f-strings 
# Phase 1 -> Week 1 -> Day 2

# ----------1. Creating string ----------
single = 'Hello'
double = "World"
multiline = """This is 
a multiline
string"""
raw = r"C:\Users\Ajay\Documents"  #backslash is literal

print(single)
print(double)
print(multiline)
print(raw)

# ---------- 2.f-string ----------

name = "Ajay"
age = 22
city = "Hisar"
price = 10000000

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"I live in {city}")
print(f"Next year I will be {age + 1}")  # math inside {}
print(f"Price with 18%GST: {price * 1.18:.2f}")  # :.f = 2 decimal places

# ---------- 3.String indexing ----------
word = "Python"
print(word[0]) # first charcter
print(word[1]) # second character
print(word[-1]) #last character
print(word[-2]) # second from last

# ---------- 4.String slicing ----------
print(word[0:3]) # Pyt
print(word[2:])  # thon
print(word[:4])  # Pyth
print(word[::2]) # every 2nd character
print(word[::-1]) # reversed

# ---------- 5. string methods ----------
sentence = " Hello World from Python "

print(sentence.upper())
print(sentence.lower())
print(sentence.strip())   # removes leading/trailing spaces
print(sentence.strip().replace("Python", "AI"))
print(sentence.strip().split(" "))  # splits into list

words = ["AI", "ML", "Python"]
print(" ".join(words))  # joins list into string

# ---------- Useful checks ----------
email = "ajay@gmail.com"
number = "12345"

print(email.startswith("ajay")) #True
print(email.endswith(".com")) # True
print(email.find("@"))         # index of @ symbol
print(number.isdigit())        # True - all characters are digits
print(email.count("."))        # how many dots

# ---------- 7.String immutability ----------
original = "hello"
# original[0] = "H"  # this would cause an ERROR
fixed = "H"  + original[1:]  # correct way
print(fixed)

# ---------- 8.Importent for AI/ML ----------
# In real AI work you constantly clean text like this:
dirty_text = " Machine Learning is AMAZING!!! "
clean_text = dirty_text.strip().lower().replace("!!!", "")
print(clean_text)
