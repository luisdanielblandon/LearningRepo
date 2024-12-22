#Started at 6:04 PM

iterator = 0
gradebook_iterator = 0

student_grades = {}

while iterator != 3:

      if iterator == 0:
            print("What would you like to do? Please type a number to continue.\n\n")
            print("1. Add students and grades\n")
            print("2. Print a student's name and grade.\n")
            print("3. Close the application.\n")
            iterator = int(input())

      if iterator == 1:
            print("\nYou are adding new students and grades.\n")
            student_name = input("What is their name? (First and Last)\n")
            student_grade = float(input("What is their grade?\n"))
            student_grades[student_name] = student_grade
            iterator = int(input("\nWould you like to add another student? 1 for Yes, 0 for No."))

      if iterator == 2:
            print("\nHere's a printout of all student grades:\n")
            print(student_grades)
            iterator = 0
            break

      if iterator == 3:
            print("Thank you! Goodbye.")
            break

#Create dictionary to store student name:grade
# create functionality to ask for the name/grade
# create function to print and finally function to quit

#Paused at 6:08 PM

#Resumed at 10:52 PM

#Paused at 11:08 PM

#Resumed at 11:22 AM

#Completed at 11:29 AM

#Total time: 27 minutes