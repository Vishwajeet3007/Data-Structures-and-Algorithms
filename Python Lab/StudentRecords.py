"""
You are a teacher at a high school, and you're responsible for maintaining the records of student 
grades. To streamline this process, you decide to create a Python program that can manage 
student records efficiently. Each student record includes the student's name, ID, and grades for 
three subjects: Math, Science, and English. You want to implement a feature that allows you to 
sort the student records based on their average grades. 
"""

class Student:
    def __init__(self, name, student_id, math, science, english):
        self.name = name
        self.student_id = student_id
        self.grades = {
            'Math': math,
            'Science': science,
            'English': english
        }
    
    def average_grade(self):
        return sum(self.grades.values()) / len(self.grades)
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Grades: {self.grades}, Average: {self.average_grade():.2f}"


class StudentRecords:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, student_id, math, science, english):
        student = Student(name, student_id, math, science, english)
        self.students.append(student)
    
    def sort_by_average_grade(self):
        self.students.sort(key=lambda student: student.average_grade(), reverse=True)
    
    def display_students(self):
        for student in self.students:
            print(student)
    

def main():
    records = StudentRecords()
    
    while True:
        print("\n--- Student Records Menu ---")
        print("1. Add student")
        print("2. Sort students by average grade")
        print("3. Display students")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            math = float(input("Enter Math grade: "))
            science = float(input("Enter Science grade: "))
            english = float(input("Enter English grade: "))
            records.add_student(name, student_id, math, science, english)
        elif choice == '2':
            records.sort_by_average_grade()
            print("Students sorted by average grade.")
        elif choice == '3':
            records.display_students()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
