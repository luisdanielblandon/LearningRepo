# (1) The program starts by asking the user to enter a directory path.
# (2) After the user enters a directory (e.g., /Users/as/Downloads), the program asks
# the user to enter a search term (e.g., “.png”).
# (3) Finally, the program lists all the file paths contained in the given directory.
# Requires libraries: os and glob

import os, glob

# Ask the user to enter a directory path
directory = input("Enter a directory path: ")

# Ask the user to enter a search term
search_term = input("Enter a search term: ")

# Use glob to find all files in the target directory with the search term
files = glob.glob(os.path.join(directory, f"*{search_term}*"))

# List all the file paths contained in the given directory
for file in files:
    print(file)
    
# Started at 3:49 AM
# Completed at 3:53 AM

# Tested with directory "/Users/luisb/Library/CloudStorage/GoogleDrive-luisdanielblandon@gmail.com/
# My Drive/python_work/LearningRepo/DailyPython/File Manipulation Exercises"
# and search term ".txt" and it worked as expected.