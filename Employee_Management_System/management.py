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

    def view_emp(self):
        if not self.total_emp.values():
            print('No records found..')
        else:
            for employee in self.total_emp.values():
                employee.display()
        
        print(f'Total employees are: {Employee.total_employees}')

    
    def update_emp(self):
        try:
            emp_id = int(input('Enter employee id to update his/her details: '))
            if emp_id in self.total_emp:
                employee = self.total_emp[emp_id]

                while True:
                    print('-' * 30)
                    print('1. Change Id')
                    print('2. Change Name')
                    print('3. Change Address')
                    print('4. Change Salary')
                    print('5. Exit')
                    print('-' * 30)

                    try:
                        choice = int(input('What do you want to update from above..'))

                        if choice == 1:
                            while True:
                                try:
                                    new_id = int(input('Enter new employee id: '))
                                    if new_id in self.total_emp:
                                        print('This id already exists..')
                                    else:
                                        employee.emp_id = new_id
                                        self.total_emp[new_id] = self.total_emp.pop(emp_id)
                                        emp_id = new_id
                                        print('Id updated Successfully..')
                                except ValueError:
                                    print('ID must be a number')

                        elif choice == 2:
                            while True:
                                new_name = input('Enter new name: ')
                                pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
                                if re.match(pattern, new_name):
                                    employee.name = new_name
                                    print('Name changed successfully..')
                                    break
                                else:
                                    print('Name must be a string..')

                        elif choice == 3:
                            while True:
                                new_address = input('Enter new address: ')
                                pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
                                if re.match(pattern, new_address):
                                    employee.address = new_address
                                    print('Address updated successfully..')
                                    break
                                else:
                                    print('Address must be a string..')
                        elif choice == 4:
                            while True:
                                try:
                                    new_salary = int(input('Enter new salary: '))
                                    if new_salary <= 0:
                                        print('Salary cannot be 0')
                                    else:
                                        employee.salary = new_salary
                                        print('Salary updated successfully..')
                                        break
                                except ValueError:
                                    print('Salary must be a number..')
                        
                        elif choice == 5:
                            break

                        else:
                            print('Invalid Choice..')
                    except ValueError:
                        print("Choice must be a number..")
            else:
                print('Id does not exists..')
        except ValueError:
            print('Employee id must be a number..')
    
    def delete_emp(self):
        while True:
            try:
                emp_id = int(input('Enter the employee id to delete him/her: '))
                if not emp_id in self.total_emp:
                    print("Employee not found to delete..")
                else:
                    self.total_emp.pop(emp_id)
                    Employee.total_employees -=1
                    print('Employee deleted successfully..')
                    break
            except ValueError:
                print("ID must be a number..")