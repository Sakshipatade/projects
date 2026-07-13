from management import StudentManagement

sms = StudentManagement()
sms.load_students()

while True:
    print('-----------Student Management System---------------')
    print('1. Add Student')
    print('2. View Student')
    print('3. Search Student')
    print('4. Update Student')
    print('5. Delete Student')
    print('6. Save Student Data')
    print('7. Exit')
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
        sms.delete_student()
    elif choice == 6:
        sms.save_students()
        print('Data Saved Successfully..')
    elif choice == 7:
        break
    else:
        print('Invalid Choice Entered..')