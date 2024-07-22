

import std  
import attend  

def main():
    while True:
        print("Attendance Management System")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")
        ch = input("Enter Your Choice: ")

        if ch == '1':
            std_id = input("Enter The Student ID: ")
            name = input("Enter The Student Name: ")
            std.add_student(std_id, name)  

        elif ch == '2':
            std_id = input("Enter The Student ID: ")
            date = input("Enter The Date (YYYY-MM-DD): ")
            if std.get_student(std_id):  
                attend.mark_attendance(std_id, date)  
            else:
                print("Student ID Not Found")

        elif ch == '3':
            attend.view_attendance()  

        elif ch == '4':
            print("Exiting The System")
            break

        else:
            print("Invalid Choice, Please Try Again")

if __name__ == "__main__":
    main()




