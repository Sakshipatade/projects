from student import Student
import re

class StudentManagement:

    def __init__(self):
        self.all_students = {}
        

    
    def add_student(self):
        while True:
            try:
                roll_no = int(input('enter your roll number: '))
                break
            except ValueError:
                print('roll number must be a number')
        while True:
            name = input('enter your name: ')
            pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
            if re.match(pattern, name):
                break
            else:
                print('Enter Corrent Name Again!')
        while True:
            age = int(input('enter your age: '))
            if age > 0:
                break
            else:
                print('Age cannot be less than 1')

        while True:
            marks = int(input('enter your marks: '))
            if marks < 100:
                break
            else:
                print("marks can't be greater than 100")

        student = Student(roll_no, name, age, marks)
        self.all_students[roll_no] = student
        print('Student Added Successfully..')

    def view_student(self):
        if not self.all_students:
            print('No students are there')
        else:
            for student in self.all_students.values():
                student.display()

        print(f'Total students are {Student.total_students}')

    # def search_student(self):
