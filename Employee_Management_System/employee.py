class Employee:
    employees = 0

    def __init__(self, emp_id, name, address, salary):
        self.emp_id = emp_id
        self.name = name
        self.address = address
        self.salary = salary

    def display(self):
        print("-" * 20)
        print(f'Employee id: {self.emp_id}')
        print(f'Employee Name: {self.name}')
        print(f'Employee Address: {self.address}')
        print(f'Employee Salary: {self.salary}')
        print('-' * 20 )
