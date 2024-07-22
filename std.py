students={}
def add_student(student_id,name):
    if student_id in students:
        print("student with ID{student_id}already exists")
    else:
        students[student_id]=name
        print("student{name}added successfully")
def get_student(student_id):
    return students.get(student_id,None)
