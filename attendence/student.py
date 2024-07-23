class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, student_name):
        student = Student(student_id, student_name)
        self.students.append(student)
        print(f"Student {student_name} added successfully.")

    def view_all_students(self):
        if not self.students:
            print("No students registered.")
        else:
            print("\nList of Students:")
            for student in self.students:
                print(f"ID: {student.student_id}, Name: {student.student_name}")

# Initialize a global instance of StudentDatabase
student_db = StudentDatabase()
