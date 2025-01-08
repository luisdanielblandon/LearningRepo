# (1) The program starts by prompting the user to enter the time
# in seconds (e.g., 10 seconds). (2) Then, the program starts
# printing out the seconds (e.g., 00:10, 00:09, etc.) one line
# every one second. (3) At the end, the program prints out
# “Time is up!”

# Required libraries: time

import time

#Get time in seconds from the user, as an integer.
countdown = int(input("Enter the time in seconds (integers only): "))

#Countdown timer

while countdown >= 1:
      timeformat = '{:02d}'.format(countdown)
      print(f"{timeformat}:00", end='\n\n')
      time.sleep(1)
      countdown -= 1

print("Time is up!")

# Time started: 5:20 PM
# Time finished: 5:25 PM