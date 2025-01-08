# (1) The program starts by showing the user a menu.
# (2) The user enters a number (e.g., 1 to add a new name to the text file)
# and then proceeds with the instructions (e.g., adding a name such as Wimbly).
# (3) The program adds that new name to the names.txt file and then shows the
# menu again. In addition to adding new names, the user can also display the
# total number of names (by pressing 2) and select a random name from the text file (by pressing 3).

#Required libraries: random, os

# Associated files:
# LearningRepo/DailyPython/Simple%20Exercises/1113_names.txt

import random, os

script_dir = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = os.path.join(script_dir, '1113_names.txt')

def add_name():
      name = input("Enter a name: ") # On the next line, I have to first identify using os the relative path to the file
      with open(FILE_PATH, "a") as file:
            file.write(name + "\n")
      print("Name added successfully!")
      show_menu()
      
def total_names():
      with open(FILE_PATH, "r") as file:
            names = file.readlines()
            print(f"Total names: {len(names)}")
      show_menu()
      
def random_name():
      with open(FILE_PATH, "r") as file:
            names = file.readlines()
            print(f"Random name: {random.choice(names)}")
      show_menu()
      
def show_menu():
      print("\n1. Add a new name\n2. Display total names\n3. Pick a random name\nType 'exit' to quit the app")
      choice = input("Enter your choice: ")
      if choice == "1":
            add_name()
      elif choice == "2":
            total_names()
      elif choice == "3":
            random_name()
      elif choice == "exit":
            print("Goodbye!")
      else:
            print("Invalid choice. Please try again.")
            show_menu()
            
            
show_menu() # This is the first function that is called when the program starts.

# Started at 2:44 AM
# Finished at 2:52 AM
# With assistance from Github Copilot

# Issue: file could not be read because the file path was incorrect. Copilot did not recognize.
# Fix: OS library is now being used to obtain the correct file path.

# Tested with name "Nebbudchadnezzar" and it was successfully added to the file.