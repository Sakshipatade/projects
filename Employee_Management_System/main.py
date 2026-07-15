from management import EmpManagement

ems = EmpManagement()

print('-' * 20)
print('1. Add Employee')
print('2. Search Employee')
# print('3. Search Employee')
# print('4. Update Employee')
# print('5. Delete Employee')
print('3. Exit')
print('-' * 20)

while True:
    choice = int(input('Enter your choice from above: '))

    if choice == 1:
        ems.add_emp()
    elif choice == 2:
        ems.search_emp()
    elif choice == 3:
        break
    else:
        print('Invalid Choice..') 
