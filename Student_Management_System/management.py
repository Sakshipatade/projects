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

    def search_student(self):
        roll_no = int(input('enter the roll number you want to search: '))
        if roll_no in self.all_students:
            for student in self.all_students.values():
                student.display()
        else:
            print('roll number not found..')

    def update_student(self):

        while True:
         
         print('1. Roll Number')
         print('2. Name')
         print('3. Age')
         print('4. Marks')

         choice = int(input('what do you want to change: '))


         if choice == 1:
            roll_no = int(input('Enter previous roll number: '))

            if roll_no in self.all_students:
                new_roll_number = int(input('Enter new roll number: '))
                self.all_students[roll_no] = new_roll_number
                
            else:
                print('entered roll number not found to change..')
            print('Roll Number changed successfully..')
            break
         
         elif choice == 2:
            name = input('Enter previous name of student: ')

            if name in self.all_students:
                new_name = input('Enter new name of student: ')
                self.all_students[name] = new_name
            else:
                print('entered name not found to change..')
            print('Name changed successfully..')
            break

         elif choice == 3:
            age = int(input('Enter previous age of student: '))

            if age in self.all_students:
                new_age = input('Enter new age of student: ')
                self.all_students[age] = new_age
            else:
                print('entered age not found to change..')
            print('Age changed successfully..')
            break
        
         elif choice == 4:
            marks = int(input('Enter previous marks of student: '))

            if marks in self.all_students:
                new_marks = input('Enter new marks of student: ')
                self.all_students[marks] = new_marks
            else:
                print('entered marks not found to change..')
            print('Marks changed successfully..')
            break
         else:
             break
         


'''
I think we need to update the dictionary each time
and for every specific roll number because it acts like unique id for each student so update the 
data of that specific student is necessary 
'''