# Day 21 - Dataclasses
# Phase 1 -> Week 3-4 -> Day 21

from dataclasses import dataclass, field
from datetime import datetime

# ---------- 1. Basic dataclass ----------
print("=== PART 1: Basic Dataclass ===")

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0    # default value

p1 = Point(1.0, 2.0, 3.0)
p2 = Point(4.0, 5.0)
p3 = Point(1.0, 2.0, 3.0)

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1 == p3: {p1 == p3}")
print(f"p1 == p2: {p1 == p2}")


# ---------- 2. Dataclass vs regular class comparison ----------
print("n=== PART 2: What Gets Auto-Generated ===")

@dataclass
class Student:
    name: str
    age:  int
    gpa:  float

s1 = Student("Alice", 21, 3.8)
s2 = Student("Bob",   22, 3.5)
s3 = Student("Alice", 21, 3.8)

print(f"s1 repr:   {s1}")
print(f"s1 == s3:  {s1 == s3}")
print(f"s1 == s2:  {s1 == s2}")

# Access fields like regular attributes
print(f"s1.name:    {s1.name}")
print(f"s1.gpa:    {s1.gpa}")

# Modify fields (unless frozen)
s1.gpa = 3.9
print(f"s1 after gpa update: {s1}")

# ---------- 3. field() - defaults and controls ----------
print("\n=== PART 3: field() ===")

@dataclass
class MLModel:
    name:          str
    model_type:    str
    learning_rate: float          = 0.001
    epochs:        int            = 10
    layers:        list           = field(default_factory=list)
    tags:          dict           = field(default_factory=dict)
    is_trained:    bool           = field(default=False, repr=False)
    created_at:    str            = field(
                                      default_factory=lambda: datetime.now().strftime("%Y-%m-%d"),
                                      repr=False
                                    )

m1 = MLModel("ResNet50", "CNN")
m2 = MLModel("BERT", "transformer", learning_rate=0.0001, epochs=3)

print(f"m1: {m1}")
print(f"m2: {m2}")

m1.layers.append("conv1")
m1.layers.append("conv2")
m1.tags["dataset"] = "ImageNet"

m2.layers.append("attention")
m2.layers.append("feedforward")

print(f"\nm1 layers: {m1.layers}")
print(f"m2 layers: {m2.layers}")
print(f"m1 tags:   {m1.tags}")
print(f"m1 created: {m1.created_at}")


# ---------- 4. frozen=True - immutable config ----------
print("\n=== PART 4: frozen=True ===")

@dataclass(frozen=True)
class TrainingConfig:
    model_name:    str
    learning_rate: float = 0.001
    batch_size:    int   = 32
    epochs:        int   = 10
    seed:          int   = 42

config = TrainingConfig("ResNet50", learning_rate=0.01, epochs=50)
print(f"Config: {config}")
print(f"lr: {config.learning_rate}")
print(f"epochs: {config.epochs}")

try:
    config.learning_rate = 0.1
except Exception as e:
    print(f"Cannot modify frozen: {type(e).__name__}: {e}")


# ---------- 5. __post_init__ - validation and derived fields ----------
print("\n=== PART 5: __post_init__ ===")

@dataclass
class Dataset:
    name:       str
    samples:    list
    test_ratio: float    = 0.2
    train_data: list     = field(init=False, repr=False)
    test_data:  list     = field(init=False, repr=False)
    num_train:  int      = field(init=False)
    num_test:   int      = field(init=False)

    def __post_init__(self):
        if not 0 < self.test_ratio < 1:
            raise ValueError(f"test_ratio must be between 0 and 1, got {self.test_ratio}")
        split = int(len(self.samples) * (1 - self.test_ratio))
        self.train_data = self.samples[:split]
        self.test_data  = self.samples[split:]
        self.num_train  = len(self.train_data)
        self.num_test   = len(self.test_data)

data = list(range(1, 101))
ds = Dataset("mnist_subset", data, test_ratio=0.2)
print(f"Dataset: {ds}")
print(f"Train samples: {ds.num_train}")
print(f"Test samples:  {ds.num_test}")
print(f"First 5 train: {ds.train_data[:5]}")
print(f"First 5 test:  {ds.test_data[:5]}")

try:
    Dataset("bad", data, test_ratio=1.5)
except ValueError as e:
    print(f"ValueError: {e}")


# ---------- 6. AI/ML use case — experiment tracking ----------
print("\n=== PART 6: AI/ML Use Case — Experiment Tracking ===")

@dataclass
class ExperimentResult:
    experiment_id: int
    model_name:    str
    accuracy:      float
    loss:          float
    epochs_run:    int
    notes:         str  = ""

    def __post_init__(self):
        if not 0 <= self.accuracy <= 1:
            raise ValueError(f"Accuracy must be in [0,1], got {self.accuracy}")

    def summary(self):
        print(f"  Exp #{self.experiment_id} | {self.model_name} | "
              f"acc={self.accuracy:.4f} | loss={self.loss:.4f} | "
              f"epochs={self.epochs_run}")

experiments = [
    ExperimentResult(1, "CNN_v1",     0.8823, 0.3421, 20),
    ExperimentResult(2, "CNN_v2",     0.9134, 0.2341, 30),
    ExperimentResult(3, "ResNet50",   0.9456, 0.1823, 50),
    ExperimentResult(4, "EfficientNet", 0.9521, 0.1654, 40, "best so far"),
    ExperimentResult(5, "MobileNet",  0.9102, 0.2987, 25),
]

print("All experiments:")
for exp in experiments:
    exp.summary()

best = max(experiments, key=lambda e: e.accuracy)
print(f"\nBest experiment: #{best.experiment_id} — {best.model_name}")
print(f"Notes: '{best.notes}'")

sorted_exps = sorted(experiments, key=lambda e: e.accuracy, reverse=True)
print("\nRanked by accuracy:")
for i, exp in enumerate(sorted_exps, 1):
    print(f"  #{i} {exp.model_name:<15} acc={exp.accuracy:.4f}")   