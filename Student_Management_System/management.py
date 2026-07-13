from student import Student
import re

class StudentManagement:

    def __init__(self):
        self.all_students = {}
        

    
    def add_student(self):
        while True:
            try:
                roll_no = int(input('enter your roll number: '))
                if roll_no in self.all_students:
                    print('Roll number already exits..')
                else:
                    break
            except ValueError:
                print('roll number must be a number')

        while True:
            name = input('enter your name: ')
            pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
            if re.match(pattern, name):
                break
            else:
                print('Enter Corrent Name Again with String Characters only!')

        while True:
            try:
                age = int(input('enter your age: '))
                if age > 0:
                    break
                else:
                    print('Age cannot be less than 1')
            except ValueError:
                print('Age must be a number..')


        while True:
            try:
                marks = int(input('enter your marks: '))
                if marks <= 100 and marks >= 0:
                    break
                else:
                    print("marks can't be greater than 100")
            except ValueError:
                print('Marks must be a number..')


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
        try: 
            roll_no = int(input('enter the roll number for the details of the student: '))
            if roll_no in self.all_students:
                student = self.all_students[roll_no]
                student.display()
            else:
                print('Student not found..')
        except ValueError:
            print('Enter integer only..')

    def update_student(self):
        try:
            roll_no = int(input('Enter the roll number of the student you want to update about his data: '))

            if roll_no in self.all_students:
                student = self.all_students[roll_no]

                while True:
                    print('.'* 20)
                    print('1. Roll Number')
                    print('2. Name')
                    print('3. Age')
                    print('4. Marks')
                    print('5. Exit')
                    print('.'* 20)

                    try:
                        choice = int(input('what do you want to change: '))


                        if choice == 1:
                            while True:
                                try:
                                    new_roll_number = int(input("Enter new roll number: "))
                                    if new_roll_number in self.all_students:
                                        print('Roll number already exits..')
                                    else:
                                        student.roll_no = new_roll_number
                                        self.all_students[new_roll_number] = self.all_students.pop(roll_no)
                                        print('Roll number changed successfully...')
                                        roll_no = new_roll_number
                                        break
                                except ValueError:
                                    print('New Roll Number must be a number..')

                        elif choice == 2:
                            while True:
                                new_name = input('Enter new name of student: ')
                                pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
                                if re.match(pattern, new_name):
                                    student.name = new_name
                                    print('Name changed successfully..')
                                    break
                                else:
                                    print('Name must be a string..')
                        
                        elif choice == 3:
                            while True:
                                try:
                                    new_age = int(input('Enter new age of student: '))
                                    if new_age <= 0:
                                        print('Age must me greater than 0')
                                    else:
                                        student.age = new_age
                                        print('Age changed successfully..')
                                        break
                                except ValueError:
                                    print('Age Must be a number..')
                        
                        elif choice == 4:
                            while True:
                                try:
                                    new_marks = int(input('Enter new marks of student: '))
                                    if new_marks >= 0 and new_marks <= 100:
                                        student.marks = new_marks
                                        print('Marks changed successfully..')
                                        break
                                    else:
                                        print('Marks must be in range between 0 to 100')
                                except ValueError:
                                    print('Marks must be a number..')
                        elif choice ==5:
                            break
                        else:
                            print('Invalid choice. Please enter a number between 1 and 5.')

                    except ValueError:
                        print('Choice must be a number..')    
            else:
                print('Roll Number not found..')
        except ValueError:
            print('Roll Number must be a number..')    
           

