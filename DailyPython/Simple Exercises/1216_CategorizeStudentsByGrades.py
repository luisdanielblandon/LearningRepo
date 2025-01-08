# Add some code after the above dictionary. The code should create a
# new dictionary that categorizes students into "Pass" or "Fail" based
# on their grades. Consider a grade of 50 or higher as "Pass" and below
# 50 as "Fail." Once you create a dictionary, use a for-loop to iterate
# over the new dictionary and print out each pair of key and value as
# below:
# Alice: Pass
# Bob: Fail
# etc.

grades = {
    "Alice": 78,
    "Bob": 42,
    "Charlie": 65,
    "Diana": 49,
    "Eve": 90
}

students = {}

for student in grades:
      if grades[student] >= 50:
            students[student] = "Pass"
      elif grades[student] <= 49:
            students[student] = "Fail"
            
for student in students:
      print(f"{student}: {students[student]}")
      
# Started at 6:46 PM
# Finished at 6:51 PM
# No help! Yay!