# The program starts by greeting the user, and letting them know they can
# type “bye” to exit the program.

# The user can ask simple questions such as “what’s the time” or “what is
# Python” and the chatbot responds. The answers are fetched from a Python
# dictionary inside the script:


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