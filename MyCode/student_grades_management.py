class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def display_grades(self):
        print(f"Grades for {self.name}: {self.grades}")

def main():
    student = Student("Bob")
    student.add_grade(88)
    student.add_grade(92)
    student.add_grade(79)
    student.display_grades()
    print(f"Average grade: {student.average_grade()}")

if __name__ == "__main__":
    main()
