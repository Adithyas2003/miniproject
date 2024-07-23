from datetime import datetime
from student import student_db
from attendance import mark_attendance, generate_report

attendance_list = []

def main():
    print("\nAttendance Management System")
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. View All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_db.add_student(student_id, student_name)
        elif choice == '2':
            student_id = input("Enter student ID to mark attendance: ")
            while True:
                date_str = input("Enter The Date (YYYY-MM-DD): ")
                try:
                    date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Invalid date format. Please enter date in YYYY-MM-DD format.")
            mark_attendance(student_id, attendance_list, date)
        elif choice == '3':
            generate_report(attendance_list)
        elif choice == '4':
            student_db.view_all_students()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
