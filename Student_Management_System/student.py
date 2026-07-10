class Student:
    total_students = 0

    def __init__(self, rollNo, name, age, marks):
        self.rollNo = rollNo
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        return f'Roll No: {self.rollNo} \nName: {self.name} \nAge: {self.age} \nMarks: {self.marks}'
    
    
    
# s = Student(42, 'sakshi', 21, 90)
# print(s.display())