# The program starts by greeting the user, and letting them know they can
# type “bye” to exit the program.

# The user can ask simple questions such as “what’s the time” or “what is
# Python” and the chatbot responds. The answers are fetched from a Python
# dictionary inside the script:

import datetime

# Define some responses for keywords
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What’s on your mind?",
    "weather": "I'm not sure about the weather, but it’s always a good day to code!",
    "time": f"The current time is {datetime.datetime.now().strftime('%H:%M')}.",
    "day": f"Today is {datetime.datetime.now().strftime('%A')}.",
    "python": "Python is a versatile programming language, great for web development, data science, and more.",
    "bye": "Bye! Have a great day!",
}

# You can start with the above dictionary and implement the rest of the program.

#Required libraries: datetime

def chatbot():
      print("Welcome to the chatbot! You can type 'bye' to exit the program.")
      while True:
            user_input = input("You: ").lower()
            for word in user_input.split():
                  word = word.strip(".,!?")
                  if word in responses:
                        print(f"Bot: {responses[word]}")
                        if word == "bye":
                              return
                        break
            else:
                  print("Bot: I'm not sure how to respond to that.")
                  
chatbot()

# Started at 5:11 AM
# Finished at 5:18 AM