# For today’s project, we utilize the Google generative
# AI API. We integrate the code with Tkinter to come up
# with graphical user interface (GUI).

# The program is a large text field where the chat (including
# responses) live.
# Below the text field is an entry field where the user types
# their message.
# When the user presses Enter, the program sends the message
# to the Google AI API and displays the response in the text
# field.

# Required libraries: tkinter, requests, json, google.generativeai

import tkinter as tk
from tkinter import scrolledtext
import requests
import json
import google.generativeai as genai

# Initialize the Google AI API client
genai.configure(api_key='KEY_REMOVED_FOR_SECURITY')
model = genai.GenerativeModel("gemini-1.5-flash")

def send_message():
    message = entry.get()
    entry.delete(0, tk.END)
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, f'You: {message}\n')
    chat.config(state=tk.DISABLED)
    chat.yview(tk.END)
    
    # Send the message to the Google AI API and get the response
    response = model.generate_content(message)
    
    # Truncate the response to only the response text
    response_text = response.candidates[0].content.parts[0].text
    
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, f'Bot: {response_text}\n')
    chat.config(state=tk.DISABLED)
    chat.yview(tk.END)

# Create the main window
root = tk.Tk()
root.title("Gemini Chatbox")

# Create the chat display area
chat = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD)
chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create the entry field for user input
entry = tk.Entry(root)
entry.pack(padx=10, pady=10, fill=tk.X)
entry.bind("<Return>", lambda event: send_message())

# Start the main event loop
root.mainloop()