# Day 7 - Week 1 Review + Comprehensions
# Phase 1 -> Week 1 -> Day 7

# ---------- PART 1 - LIST COMPREHENSIONS 

# ---------- Basic comprehension ----------
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

cubes = [x**3 for x in range(1, 6)]
print("Cubes:", cubes)

# ---------- With condition ----------
scores = [85, 92, 45, 78, 95, 33, 88, 61, 74, 90]

passed = [s for s in scores if s >= 60]
print("Passed:", passed)

failed = [s for s in scores if s < 60]
print("Failed:", failed)

high_scores = [s for s in scores if s >= 80]
print("High scores:", high_scores)

# ---------- Transform items ----------
# normalize to 0-1 range - real ML preprocessing
normalized = [s/100 for s in scores]
print("Normalized:", normalized)

# convert to grade letters
grades = ["A" if s >= 90 else "B" if s >=80
          else "C" if s >= 70 else "D" if s >=60
          else "F" for s in scores]
print("Grades:", grades)

# ---------- String comprehensions ----------
words = ["machine", "learning", "is", "powerful", "and", "fun"]

upper_words = [w.upper() for w in words]
print("Upper:", upper_words)

long_words = [w for w in words if len(w) > 4]
print("Long words:", long_words)

word_lengths = {w: len(w) for w in words}
print("Word lengths:", word_lengths)

# ---------- PART 2 - DICT COMPREHENSIONS ----------

# ----------Basic dict comprehension ----------
square_dict = {x: x**2 for x in range(1, 6)}
print("\nSquare dict:", square_dict)

# ---------- Filter dict ----------
subject_scores = {
    "Python": 95,
    "Mathematics": 72,
    "Statistics": 88,
    "Linear Algebra": 65,
    "Deep Learning": 91
}

passed_subjects = {k: v for k, v in subject_scores.items() if v >= 80}
print("Passed subjects:", passed_subjects)

failed_subjects = {k: v for k, v in subject_scores.items() if v <80}
print("Failed subjects:", failed_subjects)

# ---------- Transform dict values ----------
normalized_scores = {k: v/100 for k, v in subject_scores.items()}
print("Normalized scores:", normalized_scores)

# ---------- PART 3 - WEEK 1 REVIEW EXCERCISES 
# Comnines: variables, strings, lists, dicts, control
# flow, functions, comprehensions

# ---------- Exercise 1: Student report card ----------
def generate_report(student_name, scores_dict):
    """
    Generates a complete report card for a student.
    scores_dict: dictionary of subject:score pairs
    """
    print(f"\n{'='*40}")
    print(f" REPORT CARD - {student_name.upper()}")
    print(f"{'='*40}")

    total = 0
    for subject, score in scores_dict.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f" {subject:<20} {score:>3}  Grade: {grade}")
        total += score
    
    average = total/len(scores_dict)
    print(f"{'-'*40}")
    print(f"  Average Score:       {average:.2f}")
    print(f"  Total Subjects:      {len(scores_dict)}")
    passed = len([s for s in scores_dict.values() if s >= 60])
    print(F"  Passed:               {passed}")
    print(f"  Failed:               {len(scores_dict) - passed}")
    print(f"{'='*40}")
    return average

ajay_scores = {
    "Python":         95,
    "Mathematics":    72,
    "Statistics":     88,
    "Linear Algebra": 65,
    "Deep Learning":  91
}

avg = generate_report("Ajay Sidhu", ajay_scores)

# ---------- Ecercise 2: Word frequency analyzer ----------
def analyze_text(text):
    """
    Analyzes text and returns frequency statistics.
    Real NLP preprocessing pattern.
    """
    # clean and split
    words = text.lower().strip().split()
    clean_words = [w.replace(",", "").replace(".", "")
                   for w in words]

    # count frequencies
    freq = {}
    for word in clean_words:
        freq[word] = freq.get(word, 0) + 1

    # sort by frequency
    sorted_freq = dict(sorted(freq.items(),
                        key=lambda x: x[1], reverse=True))
    
    print(f"\nText Analysis:")
    print(f"  Total words:   {len(clean_words)}")
    print(f"  Unique words:  {len(freq)}")
    print(f"  Top 3 words:  {list(sorted_freq.items())[:3]}")
    return sorted_freq

sample = "the cat sat on the mat the cat sat and the dog sat"
analyze_text(sample)

# ---------- Exercise 3: ML data preprocessor ----------
def preprocess_dataset(data):
    """
    Preprocesses a list of numeric values.
    Demonstrates real ML data cleaning pipeline.
    """
    print(f"\nRaw data: {data}")

    # remove None values
    clean = [x for x in data if x is not None]
    print(f"After removing None: {clean}")

    # remove outliers - beyound 2 standard deviations
    mean = sum(clean) / len(clean)
    variance = sum((x - mean)**2 for x in clean) / len(clean)
    std = variance ** 0.5

    filtered = [x for x in clean if abs(x - mean) <= 2 * std]
    print(f"After outlier removal: {filtered}")

    # normalize to 0-1
    min_val = min(filtered)
    max_val = max(filtered)
    normalized = [(x - min_val)/(max_val - min_val)
                  for x in filtered]
    normalized = [round(n, 4) for n in normalized]
    print(f"Normalized: {normalized}")

    return normalized

raw_data = [23, 45, None, 67, 89, 12, None, 200, 34, 56, 78, 3]
preprocess_dataset(raw_data)