from datetime import datetime

def mark_attendance(student_id, attendance_list, date):
    attendance_list.append({
        'student_id': student_id,
        'date': date.strftime("%Y-%m-%d")
    })
    print(f"Attendance marked for student ID {student_id} on {date.strftime('%Y-%m-%d')}.")

def generate_report(attendance_list):
    if not attendance_list:
        print("No attendance records found.")
    else:
        print("\nAttendance Report:")
        for attendance in attendance_list:
            print(f"Student ID: {attendance['student_id']}, Date: {attendance['date']}")
