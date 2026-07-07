# Day 14 - Classes and Objects
# Phase 1 -> Week 3-4 -> Day 14

# ---------- 1. Basic class definition ----------
print("=== PART 1: Basic Class ===")

class Dog: 
    # class variable - shared by all Dog objects
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        # instance variables - unique to each Dog object
        self.name = name 
        self.age = age
        self.breed = breed

    def bark(self):
        return f"{self.name} says: Woof!"
    
    def description(self):
        return f"{self.name} is {self.age} years old ({self.breed})"

#Creating objects (instances)
dog1 = Dog("Bruno", 3, "Labrador")
dog2 = Dog("Max",   5, "German Shepherd")

print(dog1.bark())
print(dog2.bark())
print(dog1.description())
print(dog2.description())
print(f"Both are species: {Dog.species}")
print(f"dog1 species: {dog1.species}")

# --------- 2. __init__ in depth ----------
print("\n=== PART 2: __init__ in Depth ===")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height
    
    def scale(self, factor):
        self.width *= factor
        self.height *= factor

r1 = Rectangle(4, 6)
r2 = Rectangle(5, 5)

print(f"r1 area:      {r1.area()}")
print(f"r1 perimeter: {r1.perimeter()}")
print(f"r1 is square: {r1.is_square()}")
print(f"r2 is square: {r2.is_square()}")

r1.scale(2)
print(f"r1 after scale(2): width={r1.width}, height={r1.height}")

# ---------- 3. Instance variables vs class variable ----------
print(f"\n=== PART 3: Instance vs Class Variables ===")

class MLModel:
    # class variable - tracks how many models have been created
    model_count = 0

    def __init__(self, name, model_type):
        self.name        = name
        self.model_type = model_type
        self.is_trained  = False
        MLModel.model_count += 1   # increment class variable

    def train(self):
        self.is_trained = True
        print(f"  {self.name} has been trained.")

    def predict(self, data):
        if not self.is_trained:
            raise RuntimeError(f"{self.name} must be trained before predicting.")
        return f"  {self.name} predicts on {data}"
    
model1 = MLModel("LinearReg", "regression")
model2 = MLModel("RandomForest", "classification")
model3 = MLModel("XGBoost", "classification")

print(f"Total models created: {MLModel.model_count}")
print(f"model1 trained: {model1.is_trained}")

model1.train()
print(f"model1 trained: {model1.is_trained}")
print(model1.predict("test_data"))

try:
    print(model2.predict("test_data"))
except RuntimeError as e:
    print(f"  Error caught: {e}")

# ---------- 4. Methods that return self - method chaining ----------

print("\n=== PART 4: Data Pipeline Class ===")

class DataPipeline:
    def __init__(self, data):
        self.data = data
        self.steps = []

    def remove_negatives(self):
        self.data = [x for x in self.data if x >= 0]
        self.steps.append("remove_negatives")
        return self
    
    def normalize(self):
        if not self.data:
            return self
        min_val    = min(self.data)
        max_val    = max(self.data)
        if max_val != min_val:
            self.data = [(x - min_val) / (max_val - min_val) for x in self.data]
        self.steps.append("normalize")
        return self
    
    def round_values(self, decimals=3):
        self.data = [round(x, decimals) for x in self.data]
        self.steps.append("round_values")
        return self
    def summary(self):
        print(f"  Pipeline steps: {self.steps}")
        print(f"  Data: {self.data}")

raw_data = [1, -3, 45, 0, 88, -12, 23, 56, 100, -1]

pipeline = DataPipeline(raw_data)
pipeline.remove_negatives().normalize().round_values().summary()

# ---------- 5. AI/ML use case - Dataset class ----------
print("\n=== PART 5: AI/ML Use Case - Dataset Class ===")

class Dataset:
    def __init__(self, name, data):
        self.name    = name
        self.data    = data
        self.labels  = []

    def add_labels(self, labels):
        if len(labels) != len(self.data):
            raise ValueError("Labels count must match data count")
        self.labels = labels
    
    def size(self):
        return len(self.data)

    def split(self, test_ratio=0.2):
        split_idx  = int(self.size() * (1 - test_ratio))
        train_data = self.data[:split_idx]
        test_data  = self.data[split_idx:]
        return train_data, test_data
    
    def summary(self):
        print(f"  Dataset: {self.name}")
        print(f"  Size: {self.size()} samples")
        print(f"  Has labels: {len(self.labels) > 0}")
        train, test = self.split()
        print(f"  Train/Test split: {len(train)}/{len(test)}")

samples = [0.5, 1.2, 0.8, 3.1, 2.7, 0.3, 1.9, 4.2, 0.1, 2.3]
labels  = [0, 1, 0, 1, 1, 0, 1, 1, 0, 1]

ds = Dataset("sample_dataset", samples)
ds.add_labels(labels)
ds.summary()