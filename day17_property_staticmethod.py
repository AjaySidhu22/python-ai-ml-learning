# Day 17 - @property ad @ staticmethod
# Phase 1 -> Week 3 - 4 -> Day 17

# ---------- 1. Basic @property ----------
print("=== PART 1: Basic @property ===")

class Circle:
    def __init__(self, radius):
        self._radius = radius    # private by convention

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError(f"Radius must be positive, got {value}")
        self._radius = value
    
    @property
    def area(self):
        import math
        return round(math.pi * self._radius ** 2, 4)

    @property
    def circumference(self):
        import math
        return round(2 * math.pi * self._radius, 4)
    
    def __str__(self):
        return f"Circle(radius={self._radius})"

c = Circle(5)
print(c)
print(f"radius:        {c.radius}")
print(f"area:          {c.area}")
print(f"circumference: {c.circumference}")

c.radius = 10 
print(f"\nAfter setting radius to 10:")
print(f"radius:         {c.radius}")
print(f"area:           {c.area}")

try:
    c.radius = -3
except ValueError as e:
    print(f"\nValueError caught: {e}")


# ---------- 2. @property in AI/ML - hyperparameter validation ----------
print("\n=== PART 2: @property for Hyperparameter Validation ===")

class NeuralNetwork:
    def __init__(self, name, learning_rate, dropout_rate, batch_size):
        self.name          = name
        self.learning_rate = learning_rate    # uses setter
        self.dropout_rate  = dropout_rate     # uses setter
        self.batch_size    = batch_size       # uses setter

    @property
    def learning_rate(self):
        return self._learning_rate
    
    @learning_rate.setter
    def learning_rate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Learning rate must be a number")
        if not 0 < value < 1:
            raise ValueError(f"Learning rate must be between 0 and 1, got {value}")
        self._learning_rate = value

    @property
    def dropout_rate(self):
        return self._droupout_rate
    
    @dropout_rate.setter
    def dropout_rate(self, value):
        if not 0 <= value < 1:
            raise ValueError(f"Dropout rate must be in [0, 1), got {value}")
        self._dropout_rate = value

    @property
    def batch_size(self):
        return self._batch_size
    
    @batch_size.setter
    def batch_size(self, value):
        if not isinstance(value, int) or value <1:
            raise ValueError(f"Batch size must be a positive integer, got {value}")
        self._batch_size = value

    @property
    def config(self):
        return {
            "name":          self.name,
            "learning_rate": self._learning_rate,
            "dropout_rate":  self._dropout_rate,
            "batch_size":    self._batch_size,
        }
    
    def __str__(self):
        return (f"NeuralNetwork({self.name}) | "
                f"lr={self._learning_rate} | "
                f"dropout={self._dropout_rate} | "
                f"batch={self._batch_size}")

nn = NeuralNetwork("ResNet50", 0.001, 0.3, 32)
print(nn)
print(f"Config: {nn.config}")

nn.learning_rate = 0.01
print(f"\nAfter updating lr: {nn.learning_rate}")

invalid_cases = [
    ("learning_rate", 1.5),
    ("dropout_rate",  1.0),
    ("batch_size",    0),
]

for attr, val in invalid_cases:
    try:
        setattr(nn, attr, val)
    except (ValueError, TypeError) as e:
        print(f"  {attr}={val} -> {e}")


# ---------- 3. @staticmethod ----------
print("\n=== PART 3: @staticmethod ===")

class DataValidator:
    @staticmethod
    def is_not_empty(data):
        return len(data) > 0
    
    @staticmethod
    def has_no_nulls(data):
        return all(x is not None for x in data)
    
    @staticmethod
    def is_numaric(data):
        return all(isinstance(x, (int, float)) for x in data)
    
    @staticmethod
    def validate_all(data):
        checks = {
            "not_empty":  DataValidator.is_not_empty(data),
            "no_nulls":   DataValidator.has_no_nulls(data),
            "is_numaric": DataValidator.is_numaric(data),
        }

        passed = all(checks.values())
        return passed, checks
    
data_good = [1.2, 3.4, 5.6, 7.8]
data_bad  = [1.2, None, 5.6, "hello"]

passed, checks = DataValidator.validate_all(data_good)
print(f"\nGood data - passes: {passed}")
for check, result in checks.items():
    print(f"  {check}: {result}")

passed, checks = DataValidator.validate_all(data_bad)
print(f"\nBad data - passes: {passed}")
for check, result in checks.items():
    print(f"  {check}: {result}")


# ---------- 4. @classmethod - alternative constructors ----------
print("\n=== PART 4: @classmethod ===")

class ModelConfig:
    def __init__(self, name, learning_rate, epochs, batch_size):
        self.name          = name
        self.learning_rate = learning_rate
        self.epochs        = epochs
        self.batch_size    = batch_size

    @classmethod
    def from_dict(cls, config):
        return cls(
            config["name"],
            config["learning_rate"],
            config["epochs"],
            config["batch_size"],
        )
    
    @classmethod
    def default(cls, name):
        return cls(name, learning_rate=0.001, epochs=10, batch_size=32)
    
    def __str__(self):
        return (f"ModelConfig({self.name}) | "
                f"lr={self.learning_rate} | "
                f"epochs={self.epochs} | "
                f"batch={self.batch_size}")

config1 = ModelConfig("ResNet", 0.01, 50, 64)
config2 = ModelConfig.from_dict({
    "name": "BERT", "learning_rate": 0.0001,
    "epochs": 3, "batch_size": 16
})

config3 = ModelConfig.default("MobileNet")
print(config1)
print(config2)
print(config3)