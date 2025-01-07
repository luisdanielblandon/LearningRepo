#Started at 12:41 PM

# Given a dictionary of students and their grades, write a function that returns the average grade of the class.
students_grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

# Create a function that loops over the values of the dictionary and returns the average of the values.
def average_grade(grades_dict):
    return sum(grades_dict.values()) / len(grades_dict)

print(average_grade(students_grades))

# Output: 85.0 (Tested, Verified)

# Finished at 12:45 PM
# Finished in 4 minutes