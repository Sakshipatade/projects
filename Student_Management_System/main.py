from management import StudentManagement

sms = StudentManagement()

while True:
    print('-----------Student Management System---------------')
    print('1. Add Student')
    print('2. View Student')
    print('3. Search Student')
    print('4. Update Student')
    
    # print('5. Delete Student')
    print('5. Exit')
    print("-" * 30)


    choice = int(input('enter your choice: '))

    if choice == 1:
        sms.add_student()
    elif choice == 2:
        sms.view_student()
    elif choice == 3:
        sms.search_student()
    elif choice == 4:
        sms.update_student()
    elif choice == 5:
        break
    else:
        print('Invalid Choice Entered..')