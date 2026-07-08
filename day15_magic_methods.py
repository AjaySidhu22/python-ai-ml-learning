# Day 15 - Magic Methods 
# Phase 1 -> Week 3-4 -> Day 15

# ---------- 1. __str__ and __repr__ ----------
print("=== PART 1: __str__ and __repr__ ===")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p1 = Point(3, 4)
p2 = Point(0, 0)

print(p1)            # uses __str__
print(str(p1))       # uses __str__
print(repr(p1))      # uses __repr__
print(f"Point is: {p1}")   # uses __str__ inside f-string

points = [Point(1,2), Point(3, 4), Point(5, 6)]
print(points)        # list uses __repr__ for each element


# ----------2. __len__ and __contains__ ----------
print("\n=== PART 2: __len__ and __contains__ ===")

class Vocabulary:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word.lower())

    def __len__(self):
        return len(self.words)

    def __contains__(self, word):
        return word.lower() in self.words
    
    def __str__(self):
        return f"Vocabulary({len(self)} words)"

vocab = Vocabulary()
vocab.add_word("Python")
vocab.add_word("Machine")
vocab.add_word("Learning")
vocab.add_word("Neural")
vocab.add_word("Network")

print(f"Vocabulary size: {len(vocab)}")
print(f"'python' in vocab: {'python' in vocab}" )
print(f"'Java' in vocab: {'Java' in vocab}")
print(vocab)

# ---------- 3. __eq__ and __lt__ for comparison ----------
print("\n=== PART 3: __eq__ and __lt__ ===")

class ModelResult:
    def __init__(self, name, accuracy):
        self.name     = name
        self.accuracy = accuracy

    def __repr__(self):
        return f"ModelResult(name='{self.name}', accuracy={self.accuracy})"

    def __eq__(self, other):
        return self.accuracy == other.accuracy
    
    def __lt__(self, other):
        return self.accuracy < other.accuracy
    
r1 = ModelResult("LinearRegression", 0.823)
r2 = ModelResult("RandomForest",     0.912)
r3 = ModelResult("XGBoost",          0.945)
r4 = ModelResult("SVM",              0.912)

print(f"r1 == r2: {r1 == r2}")
print(f"r2 == r4: {r2 == r4}")
print(f"r1 < r2:  {r1 < r2}")
print(f"r3 < r1:  {r3 < r1}")

results = [r1, r2, r3, r4]
sorted_results = sorted(results)
print("\nModels sorted by accuracy (lowest to highest):")
for r in sorted_results:
    print(f"  {r}")

best = max(results)
print(f"\nBest model: {best}")

# ---------- 4. __add__ ----------
print("\n=== PART 4: __add__ ===")

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)  ** 0.5
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = v1 + v2

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v3}")
print(f"magnitude of v3 = {v3.magnitude():.4f}")


# ---------- 5. AI/ML use case - full model class ----------
class TrainingRun:
    def __init__(self, run_id, model_name, epochs, final_loss, accuracy):
        self.run_id      = run_id
        self.model_name  = model_name
        self.epochs      = epochs
        self.final_loss  =  final_loss
        self.accuracy    = accuracy

    def __str__(self):
        return (f"Run {self.run_id} | {self.model_name} | "
                f"epochs={self.epochs} | "
                f"loss={self.final_loss:.4f} | "
                f"acc={self.accuracy:.4f}")
    
    def __repr__(self):
        return (f"TrainingRun(run_id={self.run_id}, "
                f"model='{self.model_name}', "
                f"accuracy={self.accuracy})")

    def __eq__(self, other):
        return self.accuracy == other.accuracy
    
    def __lt__(self, other):
        return self.accuracy < other.accuracy
    
    def __len__(self):
        return self.epochs
    
runs = [
    TrainingRun(1, "CNN",         50, 0.2341, 0.9102),
    TrainingRun(2, "ResNet",      80, 0.1823, 0.9456),
    TrainingRun(3, "MobileNet",   30, 0.3102, 0.8734),
    TrainingRun(4, "EfficientNet",60, 0.1654, 0.9521),
]

print("All training runs:")
for run in runs:
    print(f"  {run}")

print(f"\nEpochs in run 1: {len(runs[0])}")

best_run = max(runs)
print(f"\nBest run: {best_run}")
print(f"Best run repr: {repr(best_run)}")

sorted_runs = sorted(runs, reverse=True)
print("\nRuns ranked best to worst:")
for i, run in enumerate(sorted_runs, start=1):
    print(f"  #{i} {run}")