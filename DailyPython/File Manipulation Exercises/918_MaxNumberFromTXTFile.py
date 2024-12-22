#Started at 11:41 AM

import random
import os

def read_numbers_from_file(file_path):
     
      maxnumber = 0

      try:
            with open(file_path, 'r') as file:
                  allnumbers = file.readlines()
            # Strip any extra whitespace characters (like newlines) from each name
            for number in allnumbers:
                  if int(number) >= int(maxnumber):
                        maxnumber = number
            return maxnumber
      except FileNotFoundError:
            print(f"The file at {file_path} was not found.")
            return []
      except Exception as e:
            print(f"An error occurred: {e}")
            return []

script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, '918_numbers.txt')

print(read_numbers_from_file(file_path))

#Finished and tested at 11:50 AM