# model.py 
# Class definitions for Student Grade Management System
# Phase 1 -> Week 3-4 -> Mini Project

from dataclasses import dataclass, field


# ---------- Grade Scale ----------

GRADE_SCALE = {
    "A": {"min": 90, "points": 4.0},
    "B": {"min": 80, "points": 3.0},
    "C": {"min": 70, "points": 2.0},
    "D": {"min": 60, "points": 1.0},
    "F": {"min":  0, "points": 0.0},
}


# ---------- Grade (dataclass) ----------

@dataclass
class Grade:
    student_id: str
    course_id:  str
    score:      float

    def __post_init__(self):
        if not 0 <= self.score <= 100:
            raise ValueError(f"Score must be between 0 and 100, got {self.score}")

    @property
    def letter_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"

    @property
    def grade_points(self):
        return GRADE_SCALE[self.letter_grade]["points"]

    def __str__(self):
        return (f"Grade(student={self.student_id}, "
                f"course={self.course_id}, "
                f"score={self.score}, "
                f"letter={self.letter_grade})")
    

# ---------- Course ----------

class Course:
    def __init__(self, course_id, course_name, credits=3):
        self.course_id   = course_id
        self.course_name = course_name
        self.credits     = credits

    @staticmethod
    def validate_credits(credits):
        return isinstance(credits, int) and 1 <= credits <=6
    
    def __str__(self):
        return f"{self.course_id}: {self.course_name} ({self.credits} credits)"

    def __repr__(self):
        return (f"Course(id='{self.course_id}'), "
                f"name='{self.course_name}', "
                f"credits={self.credits}")
    
    def __eq__(self, other):
        return self.course_id == other.course_id
    

# ---------- Person (base class) ----------

class Person:
    def __init__(self, name, email):
        self._name = name.strip().title()
        self._email = email.strip().lower()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip().title()

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError(f"Invalid email: {value}")
        self._email = value.strip().lower()
    
    def __str__(self):
        return f"{self.name} <{self.email}>"
    
    def __repr__(self):
        return f"Person(nmae='{self.name}', email='{self._email}') "


# ----------Student (inherits Person) ----------

class Student(Person):
    _id_counter = 1

    def __init__(self, name, email, student_id=None):
        super().__init__(name, email)
        if student_id:
            self.student_id = student_id
        else:
            self.student_id = f"S{Student._id_counter:03d}"
            Student._id_counter += 1
        self._grades = []

    def add_grade(self, grade):
        if not isinstance(grade, Grade):
            raise TypeError("Expexted a Grade object")
        self._grades.append(grade)

    def get_grades(self):
        return list(self.grades)

    def get_grade_for_course(self, course_id):
        for grade in self._grades:
            if grade.course_id == course_id:
                return grade
            return None
        
    @property
    def gpa(self):
        if not self._grades:
            return 0.0
        total_points = sum(g.grade_points for g in self._grades)
        return round(total_points / len(self._grades), 2)

    @property
    def grade_count(self):
        return len(self._grades)
    
    def __str__(self):
        return (f"Student({self.student_id}) - "
                f"{self._name} | GPA: {self.gpa:.2f}")
    
    def __repr__(self):
        return (f"Student(id='{self.student_id}', "
                f"name='{self._name}', "
                f"gpa={self.gpa})")
    
    def __eq__(self, other):
        return self.student_id == other.student_id

    def __lt__(self, other):
        return self.gpa < other.gpa

# ---------- Quick self-test when run directly ----------

if __name__ == "__main__":
    print("=== Testing models.py ===")

    # Test Grade
    g1 = Grade("S001", "CS101", 92.5)
    g2 = Grade("S001", "CS102", 78.0)
    g3 = Grade("S001", "CS103", 55.0)
    print(f"\nGrade 1: {g1}")
    print(f"  letter={g1.letter_grade}, points={g1.grade_points}")
    print(f"Grade 2: {g2}")
    print(f"  letter={g2.letter_grade}, points={g2.grade_points}")
    print(f"Grade 3: {g3}")
    print(f"  letter={g3.letter_grade}, points={g3.grade_points}")

    # Test Course
    c1 = Course("CS101", "Python Programming", 4)
    c2 = Course("CS102", "Data Structures", 3)
    c3 = Course("CS103", "Machine Learning", 4)
    print(f"\nCourse 1: {c1}")
    print(f"Course 2: {c2}")
    print(f"Valid credits (3): {Course.validate_credits(3)}")
    print(f"Valid credits (9): {Course.validate_credits(9)}")

    # Test Person
    p = Person("ajay sidhu", "ajay@email.com")
    print(f"\nPerson: {p}")
    print(f"  name auto-titled: {p.name}")

    try:
        p.email = "bademail"
    except ValueError as e:
        print(f"  Email error: {e}")

    # Test Student
    s1 = Student("Ajay Sidhu", "ajay@email.com")
    s2 = Student("Priya Sharma", "priya@email.com")
    s3 = Student("Rahul Verma", "rahul@email.com")

    s1.add_grade(g1)
    s1.add_grade(g2)
    s1.add_grade(g3)

    print(f"\nStudent: {s1}")
    print(f"  grade_count: {s1.grade_count}")
    print(f"  gpa: {s1.gpa}")
    print(f"  grade for CS101: {s1.get_grade_for_course('CS101')}")
    print(f"  grade for CS999: {s1.get_grade_for_course('CS999')}")

    # Test sorting
    s2.add_grade(Grade("S002", "CS101", 88.0))
    s3.add_grade(Grade("S003", "CS101", 95.0))

    students = [s1, s2, s3]
    ranked = sorted(students, reverse=True)
    print("\nStudents ranked by GPA:")
    for s in ranked:
        print(f"  {s}")

    # Test invalid grade
    try:
        Grade("S001", "CS101", 150)
    except ValueError as e:
        print(f"\nInvalid grade error: {e}")

    print("\nmodels.py — all tests passed.")