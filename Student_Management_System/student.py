class Student:
    total_students = 0

    def __init__(self, roll_no, name, age, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks
        Student.total_students += 1

    def display(self):
        print('-' * 20)
        print(f'Roll No: {self.roll_no}')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Marks: {self.marks}')
        print('-' * 20)

    
    
