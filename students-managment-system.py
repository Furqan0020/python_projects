import sys
studentsData = []
# functions
def menu():
    print("""
        Welcome to the \"Saharah School Managment system"\
        
        Enter 1 for Add Stuents \n
        Enter 2 for Display Students \n
        Enter 3 for Update Students \n
        Enter 4 for Delete Students 
    """)
def addStudents(studentsData):
    name = input("please enter student name\n")
    studentsData.insert(0, name)
    print(f"{name} is inserted in student list successfully")
def displayStudents(studentsData):
    count = 0
    print("Display Students Data\n")
    if studentsData == []:
        print("list is Empty")
        addStudents(studentsData)
    for x in studentsData:
        count=count+1
        print(f"{count} => {x}")
def updateStudents(studentsData):
    displayStudents(studentsData)
    index = int(input("enter student number that you want to updated\n"))
    index = index-1
    newName = input("enter new name\n")
    studentsData[index]=newName
    print("Student updated successfully")
    displayStudents(studentsData)
def deleteStudents(studentsData):
    displayStudents(studentsData)
    index = int(input("enter student number that you want to deleted\n"))
    index = index - 1
    del studentsData[index]
    print("Student deleted successfully")
    displayStudents(studentsData)


menu()

i = 0
while(i >= 0):
    menu()
    choice = int(input("Enter Your Choice between 1 - 4 : \n"))
    if choice == 1:
        addStudents(studentsData)
    elif choice == 2:
        displayStudents(studentsData)
    elif choice == 3:
        updateStudents(studentsData)
    elif choice == 4:
        deleteStudents(studentsData)
    repeat = input("Enter y to repeat again \n and n to exit \n")
    repeat.lower()
    if repeat == "y":
        continue
    else:
        break
