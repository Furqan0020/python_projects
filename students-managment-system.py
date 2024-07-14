import sys
students = []
courses = []
def menu():
    print('School Managment System')
    print('1 . Add Student')
    print('2 . Add Course')
    print('3 . Enroll Student in Course')
    print('4 . Display Student information')
    print('5 . Exit')
def add_student(id , name , age):
    print('add student' , id , name , age)
    students.append({})
    students[id-1]['id'] = id
    students[id-1]['name'] = name
    students[id-1]['age'] = age
   
    print(students)
    return id
 
def add_course(id , name , instructor):
    print('add course' , id  , name , instructor)
    courses.append({})
    courses[id-1]['id'] = id
    courses[id-1]['name'] = name
    courses[id-1]['instrcutor'] = instructor
    print(courses)
def enroll_student(student_id , course_id):
    print("enroll student" , student_id , course_id)
    students[student_id-1]['courses'] = courses[course_id-1]
    print(students)
def display_student_info(id):
    print('student information')
    print(students[id-1])
try:
    i = 0
    choice = "y"
    while i>=0:
        menu()
        value = int(input("Enter your choice:\n"))
        match value:
            case 1:
                std_id = int(input("Enter student id : \n"))
                std_name = input("enter student name : \n")
                std_age = input("enter student age : \n")
                add_student(std_id , std_name, std_age)
            case 2: 
                print('add course')
                course_id = int(input("enter course id : \n"))
                course_name = input("enter course name : \n")
                course_instructor = input("enter course instructor name : \n")
                add_course(course_id , course_name , course_instructor)
            case 3:
                print('enroll student')
                student_id = int(input("enter student id : \n"))
                course_id = int(input("enter course id : \n"))
                enroll_student(student_id , course_id)
            case 4:
                print('display student')
                student_id = int(input("enter student id : \n"))
                display_student_info(student_id)

            case 5:
                print('exit')
                break 
            case __:
                print('invaid input')
        choice = input("want to repeat again press 'y':\n")
        choice.lower()
        if choice == 'y':
            continue
        else:
            break

except ValueError as e:
    print('you must enter intager value')
except Exception as e:
    print('something went worng.......' , e)

   
