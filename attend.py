attendence_records={}
def mark_attendence(std_id,date):
    if date not in attendence_records:
        attendence_records[date]=[]
        attendence_records[date].append(std_id)
        print("Attendence marked for student ID{std_id}on {date}.")
def view_attendence():
    for date,student in attendence_records.items():
        print("Date:{date},Students:{students}")