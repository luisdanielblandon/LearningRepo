#Started 12:16 PM

import os

#Declare file_path and set it to the path where the python script file is located
file_path = os.path.dirname(os.path.realpath(__file__))


#Loop over all the files in the directory to identify the .TXT files
for filename in os.listdir(file_path):
      if filename.endswith('.txt'):
            with open(os.path.join(file_path, filename), 'r') as file:
                  #print the name of the TXT  file
                  print(f"Printing contents of {filename}")
                  #print each TXT file as its iterated over.
                  print(file.readlines(),"\n")

print("That's all the files!")

#Completed at 12:24 PM