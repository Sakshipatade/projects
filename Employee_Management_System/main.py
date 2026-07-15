from management import EmpManagement

ems = EmpManagement()

while True:
    print('-' * 20)
    print('1. Add Employee')
    print('2. Search Employee')
    print('3. View Employee')
    print('4. Update Employee')
    print('5. Delete Employee')
    print('6. Exit')
    print('-' * 20)


    choice = int(input('Enter your choice from above: '))

    if choice == 1:
        ems.add_emp()
    elif choice == 2:
        ems.search_emp()
    elif choice == 3:
        ems.view_emp()
    elif choice == 4:
        ems.update_emp()
    elif choice == 5:
        ems.delete_emp()
    elif choice == 6:
        break
    else:
        print('Invalid Choice..') 
