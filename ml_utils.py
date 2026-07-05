# ml_utils.py - a utility module for ML tasks
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
