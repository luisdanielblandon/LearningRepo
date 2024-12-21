# Started: 7:55 PM

import random
import os

def read_names_from_file(file_path):
      try:
            with open(file_path, 'r') as file:
                  names = file.readlines()
            # Strip any extra whitespace characters (like newlines) from each name
            names = [name.strip() for name in names]
            return names
      except FileNotFoundError:
            print(f"The file at {file_path} was not found.")
            return []
      except Exception as e:
            print(f"An error occurred: {e}")
            return []

script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, '1102_names.txt')
names = read_names_from_file(file_path)

print(f"Randomly selected name from list: {random.choice(names)}")

#Finished 8:19 PM