from employee import Employee
import re

class EmpManagement:
    def __init__(self):
        self.total_emp = {}

    def add_emp(self):
        while True:
            try:
                emp_id = int(input('Enter Employee id: '))
                if emp_id in self.total_emp:
                    print('Employee ID Already Exists..')
                else:
                    break
            except ValueError:
                print('Employee ID must be a number')

        while True:
            name = input('Enter Employee Name: ')
            pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
            if re.match(pattern, name):
                break
            else:
                print('Enter Corrent Name Again with String Characters only!')

        while True:
            address = input('Enter Employee Address: ')
            pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
            if re.match(pattern, address):
                break
            else:
                print('Enter Corrent Address Again!')
        
        while True:
            try:
                salary = int(input('Enter Employee Salary: '))
                if salary in self.total_emp:
                    print('Salary already entered.')
                else:
                    break
            except ValueError:
                print('Salary must be a number..')
        
        employee = Employee(emp_id,name,address,salary)
        self.total_emp[emp_id] = employee
        print('Employee Added Successfully..')

    def search_emp(self):
        try:
            emp_id = int(input('Enter Employee ID to view his details: '))
            if emp_id in self.total_emp:
                employee = self.total_emp[emp_id]
                employee.display()
            else:
                print('Employee does not exist..')
        except ValueError:
                print('Employee Id must be a number..')
