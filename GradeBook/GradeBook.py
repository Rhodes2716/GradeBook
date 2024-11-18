from random import choice

# I use a array dictionary to house the arrays, Name of the array is the students and the grades are the values
gradebook = {'Venni': [75.5, 81.33, 72.50], 'Evan': [79.5, 90.45, 88.50], 'Teezy': [62.81, 58.5, 99.75], 'Cyrus': [70.71, 85.57, 0.0], 'Caden': [96.7, 100.0, 89.95]}

def main(): # Constructor function, basically a main menu
    whatdo = input("What would you like to do? \n 1) Create Student \n 2) Enter Grades \n 3) Edit Grades \n 4) View Gradebook \n 5) Remove Grades \n 6) Remove Student \n")

    try: # Try this, if it fails return nothing and go back to main.
        whatdoreturn = int(whatdo) #use int to validate the data is a whole number, if it isn't it throws ValueError
    except  ValueError:
        return
    # Check for value and go to respective function, else just return to main()
    if whatdoreturn == 1:
        create()
    elif whatdoreturn == 2:
        enter()
    elif whatdoreturn == 3:
        edit()
    elif whatdoreturn == 4:
        view()
    elif whatdoreturn == 5:
        removegrade()
    elif whatdoreturn == 6:
        removestudent()
    else:
        print("Invalid input, give me a number.")
        main()

def enter(): # Enter a grade
    global gradebook
    student_name = input("Student Name: ")

    if student_name == "": # Return to main if nothing is entered.
        main()
        return

    if student_name not in gradebook:
        print("Please enter a valid name.")
        enter()
        return

    if student_name in gradebook:
       try:
           grade = float(input("Grade: "))
           gradebook[student_name].append(grade)
           print(f"Grade {grade} added to {student_name}")
       except ValueError:
           print("Invalid grade, please enter a number.")
           main()
           return
    main()

def view(): # View Gradebook
    global gradebook
    if gradebook:
        print("Current students and their grades.")
        print(gradebook)
    else:
        print("No students found")
    main()

def create(): # Create Student
    global gradebook
    bulk_question = int(input("1) One Student \n2) Many Students \n"))
    if bulk_question == 1:
        student_name = input("Name: ")
        gradebook[student_name] = []
        print(f"Student '{student_name}' added.")
    else:
        i = int(input("How many: "))
        for i in range(i): # uses i for iteratives
            student_name = input("Name: ")
            gradebook[student_name] = []
            print(f"Student '{student_name}' added.")
    main()

def edit(): # Edit Grades
    global gradebook
    student_name = input("Name of the Student:")
    if student_name in gradebook:
        old_grade = int(input("0 is the first, what grade: "))
        new_grade = float(input("New Grade: "))
        gradebook[student_name][old_grade] = new_grade
        print(f"Grade {new_grade} changed for {student_name}.")
        
    else:
        print("Name not in system.")
    main()

def removegrade (): # Remove a grade
    global gradebook
    try:
        student_name = str(input("Which Student: "))
        del_choice = int(input("0 is first, what grade: "))
        del gradebook[student_name][del_choice]
        print(f"Grade {del_choice} for {student_name} is deleted.")
    except:
        print("Invalid input.")
    main()

def removestudent(): # Remove a student
    global gradebook
    bulk_question = int(input("1) One Student \n2) Many Students \n"))
    try:
        if bulk_question == 1:
            student_name = str(input("Which Student: "))
            del gradebook[student_name]
            print(f"Student {student_name} has been deleted.")
        
        else:
            i = int(input("How Many: "))
            for i in range(i):
                student_name = str(input("Which Student: "))
                del gradebook[student_name]
                print(f"Student {student_name} has been deleted.")
    except:
        print("Invalid input.")
    main()
main()
