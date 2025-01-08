# The program starts by prompting the user to enter a deadline in
# the YYYY-MM-DD HH:MM format.
# If the submitted deadline is later than the current time and date,
# the program displays the message “The deadline is in x day(s). Keep
# working 🚀”
#
# If the submitted date is earlier than today’s date, that means the
# deadline has passed, and the message “The deadline has passed 😢”
# is printed out.

# Required libraries: datetime

import datetime

# Get the deadline from the user
deadline = input("Enter the deadline (YYYY-MM-DD HH:MM): ")

# Convert the deadline to a datetime object
deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M")

# Get the current date and time
current_time = datetime.datetime.now()

# Calculate the difference between the deadline and the current time
time_difference = deadline - current_time

# Check if the deadline has passed
if time_difference.days < 0:
    print("The deadline has passed 😢")
else:
      print(f"The deadline is in {time_difference.days} day(s). Keep working 🚀")
      
      
# Time started: 5:54 PM
# Time finished: 5:56 PM
# With assistance of Github Copilot