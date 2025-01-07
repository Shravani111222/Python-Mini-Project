#empty student grade dictionary
student_dict = {} 


def add_student():
        try:
            student_name = str(input("Enter Student Name: "))
            student_grades = (input("Enter Student Grade(comma separated): "))
                
            # Convert input into a list of integers
            grades_list = [int(grade.strip()) for grade in student_grades.split(",")]
            student_dict[student_name] = grades_list
            print("Added record for", student_name, ":", student_dict[student_name])
        
        except:
             print("Error while adding student grades, add integer values!")
        return 

def update_grade():
        try:
            student_name=str(input("Enter the student's name to update:"))

            if student_name in student_dict:
                print("Current grade:", student_dict[student_name])
                new_grade=(input("Enter new grade:"))
                student_dict[student_name]=new_grade
                print("Updated grade for",student_name,":",new_grade)
            else:
                print("Student not found")
        except:
            print("Error while adding student grades, add integer values!")
        return

def stud_avg():
        try:
            student_name = input("Enter the student's name to calculate the average grade: ")
            if student_name in student_dict:
                student_grades = student_dict[student_name]
                average = sum(student_grades) / len(student_grades)
                average = round(average, 2)
                print("The average grade for", student_name, "is:", average)
            else:
                print("Student not found.")
        except:
              print("Error while adding student grades, add integer values!")
        return

def display():
        try:
            if not student_dict:
                print("No student data available.")
            else:
                print("Student Grade Data", student_dict)
        except:
             print("Error while adding student data")
        return

# Choice 5 function
def exiting():
        print('Exiting.....!')


while True:
    # Display the menu options
    print("\nMenu:")
    print("1. Add a Student and Grades")
    print("2. Update Grades")
    print("3. Calculate Average Grades")
    print("4. Display All Students")
    print("5. Exit")

#Get the users choice
    choice=input("Enter your choice(1-5):")
    try:
 
        if choice=="1":
            add_student()
            pass

        elif choice == "2":
                update_grade()
                pass

        elif choice =="3":
            stud_avg()
            pass

        elif choice == "4":
            display()
            pass

        elif choice == "5":
            print('exitinggggggg')
            break
        
        else:
            print("Wrong Choice Selected!")
    except:
         print("Error occured")




        