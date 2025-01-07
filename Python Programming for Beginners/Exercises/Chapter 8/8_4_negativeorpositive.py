import math

def is_neg_or_pos(num_input):
      if num_input == 0:
            print("The number is zero!")
            return 0
      if num_input == abs(num_input):
            print ("The number is positive!")
            return 0
      if num_input != abs(num_input):
            print("The number is NEGATIVE ahh!")
            return 0
      

userinput = int(input("What number would you like to identify as positive, negative, or zero?\n"))

is_neg_or_pos(userinput)