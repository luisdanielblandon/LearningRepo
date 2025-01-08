# Instructions:\
      
# 1. Use glob to Find Files:
# Use the glob module to find all files in the target directory with specific patterns (like *.txt for text files).

# 2. Create Folders Based on File Type:
# For each file type, create a corresponding folder (e.g., "Text Files", "Images").

# 3. Move Files to the Appropriate Folder:
# Move the files into the appropriate folder based on their extension using shutil.move().

# Required libraries: os and glob

import os, glob

# User defines the folder where the operation should begin by inputting a directory path
dir_path = input("Enter the directory path: ")

# Change the current working directory to the user-defined directory
os.chdir(dir_path)

# Create a list of all files in the directory
files = glob.glob("*")

# Create a dictionary to store file types and their corresponding extensions
file_types = {}

# Iterate through each file in the directory
for file in files:
    # Check if the file is a directory
    if os.path.isdir(file):
        continue
    # Extract the file extension
    extension = file.split(".")[-1]
    # Check if the extension is already in the dictionary
    if extension in file_types:
        # Append the file name to the existing list
        file_types[extension].append(file)
    else:
        # Create a new list with the file name
        file_types[extension] = [file]
        
# Create a list of unique file extensions
extensions = list(file_types.keys())

# Create a folder for each unique file extension
for extension in extensions:
    # Check if the folder already exists
    if not os.path.exists(extension):
        os.mkdir(extension)
    # Move each file to the corresponding folder
    for file in file_types[extension]:
        os.rename(file, os.path.join(extension, file))
        
print("Files organized successfully!")

# Started at 3:55 AM
# Finished at 4:00 AM