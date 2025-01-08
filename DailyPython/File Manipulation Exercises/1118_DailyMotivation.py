# The program checks what day it is. If it is Monday it displays "It is Monday!"
# and picks a random quote from the quotes.txt file.
# B) Scenario 2: If not Monday
# If it is not Monday, the program displays some other text as shown below:
# "It is Tuesday! Have a great day!"

# Required libraries: random, os, datetime

# Associated files:
# LearningRepo/DailyPython/File%20Manipulation%20Exercises/1118_quotes.txt

import random, os, datetime

# Check if it is Monday
if datetime.datetime.now().strftime('%A') == "Monday":
      print("It is Monday!")
      # Open the quotes file, using os to identify the folder where 1118_quotes.txt is located
      with open(os.path.join(os.path.dirname(__file__), "1118_quotes.txt")) as file:
            quotes = file.readlines()
      # Pick a random quote
      print(random.choice(quotes))
else:
      print("It is", datetime.datetime.now().strftime('%A'), "! Have a great day!")
      

# Started at 2:56 AM
# Finished at 2:57 AM

# Copilot had to be guided to use OS library to first define the path to the quotes file.