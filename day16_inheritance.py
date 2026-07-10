# Day 16 - Inheritance and Polymorphism
# Phase 1 -> Week 3-4 -> Day 16

# ---------- 1. Basic Inheritance ----------
print("=== PART 1: Basic Inheritance ===")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound"

    def description(self):
        return f"{self.name} is {self.age} years old"

    def __str__(self):
        return f"Animal(name={self.name}, age={self.age})"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # call parent __init__
        self.breed = breed

    def speak(self):                   # override parent method
        return f"{self.name} says: Woof!" 

    def fetch(self):                   # new method only in Dog
        return f"{self.name} fetches the ball!"
    
    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed})"


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says: Meow!"

    def __str__(self):
        return f"Cat (name={self.name}, indoor={self.indoor})"


dog = Dog("Bruno", 3, "Labrador")
cat = Cat("Whiskers", 2, True)

print(dog.speak())
print(cat.speak())
print(dog.description())    # inherited from Animal
print(cat.description())    # inherited from Animal
print(dog.fetch())          # Dog-only method
print(dog)
print(cat)


# ---------- 2. isinstance() ----------
print("\n=== PART 2: isinstance() ===")

print(f"dog is Dog: {isinstance(dog, Dog)}")
print(f"dog is Animal: {isinstance(dog, Animal)}")
print(f"dog is Cat: {isinstance(dog, Cat)}")
print(f"cat is Animal: {isinstance(cat, Animal)}")


# ---------- 3. Polymorphism ----------
print("\n=== PART 3: Polymorphism ===")

animals = [
    Dog("Rex", 4, "German Shepherd"),
    Cat("Luna", 1, False),
    Dog("Max", 2, "Poodle"),
    Cat("Mochi", 3, True),
    Animal("Parrot", 5),
]

for animal in animals:
    print(f"  {animal.speak()}")


# ---------- 4. AI/ML use case - Model hierarchy ----------
print("\n=== PART 4: AI/ML - Model Hierarchy ===")

class BaseModel:
    def __init__(self,name, learning_rate=0.01):
        self.name          = name
        self.learning_rate = learning_rate
        self.is_trained    = False
        self.history       = []

    def fit(self, X, y):
        raise NotImplementedError("Subclass must implement fit()")

    def predict(self, X):
        if not self.is_trained:
            raise RuntimeError(f"{self.name} must be trained before predict()")
        raise NotImplementedError("Subclass must implement predict()")

    def evaluate(self, predictions, labels):
        correct = sum(p == l for p, l in zip(predictions, labels))
        return correct / len(labels)

    def save(self, filepath):
        print(f"  [{self.name}] Model saved to {filepath}")

    def __str__(self):
        return (f"{self.name} | lr={self.learning_rate} "
                f"trained={self.is_trained}")

    def __repr__(self):
        return f"BaseModel(name='{self.name}', lr={self.learning_rate})"


class LinearModel(BaseModel):
    def __init__(self, learning_rate=0.01):
        super().__init__("LinearModel", learning_rate)
        self.weights = []

    def fit(self, X, y):
        self.weights   = [0.5] * len(X[0])
        self.is_trained = True
        self.history.append({"epoch": 1, "loss": 0.45})
        print(f"  [{self.name}] Trained on {len(X)} samples")

    def predict(self, X):
        if not self.is_trained:
            raise RuntimeError(f"{self.name} must be trained before predict()")
        return [1 if sum(row) > 0 else 0 for row in X]

    def __str__(self):
        return f"LinearModel | weights={len(self.weights)} | trained={self.is_trained}"

    
class TreeModel(BaseModel):
    def __init__(self, max_depth=5):
        super().__init__("TreeModel", learning_rate=0.0)
        self.max_depth = max_depth

    def fit(self, X, y):
        self.is_trained = True
        self.history.append({"epoch": 1, "loss": 0.32})
        print(f"  [{self.name}] Trained with max_depth={self.max_depth}")

    def predict(self, X):
        if not self.is_trained:
            raise RuntimeError(f"{self.name} must be trained before predict()")
        return [1 if row[0] > 0.5 else 0 for row in X]

    def __str__(self):
        return f"TreeModel | max_depth={self.max_depth} | trained={self.is_trained}"

    
# Sample data
X_train = [[0.1, 0.2], [0.9, 0.8], [0.3, 0.4], [0.7, 0.6]]
y_train = [0, 1, 0, 1]
X_test  = [[0.2, 0.3], [0.8, 0.7]]
y_test  = [0, 1]

models = [LinearModel(learning_rate=0.05), TreeModel(max_depth=3)]

print("Training all models:")
for model in models:
    model.fit(X_train, y_train)

print("\nPredicting with all models:")
for model in models:
    preds    = model.predict(X_test)
    accuracy = model.evaluate(preds, y_test)
    print(f"  {model}")
    print(f"  Predictions: {preds} | Accuracy: {accuracy:.2%}")
    model.save(f"{model.name.lower()}.pkl")
    print()

# ---------- 5. isinstance() in production-style validation ----------
print("=== PART 5: isinstance() for Input Validation ===")

def run_pipeline(model, X, y):
    if not isinstance(model, BaseModel):
        raise TypeError(f"Expected BaseModel, got {type(model)}")
    model.fit(X, y)
    preds = model.predict(X)
    acc   = model.evaluate(preds, y)
    print(f"  Pipeline complete for {model.name} - accuracy: {acc:.2%}")

run_pipeline(LinearModel(), X_train, y_train)

try:
    run_pipeline("not_a_model", X_train, y_train)
except TypeError as e:
    print(f"  TypeError caught: {e}")      