# The program starts by asking the user a few questions, such as the
# desired password length, and if there have to be any uppercase letters,
# numbers, or special characters in the password. Depending on the user's
# answers, the program generates a password and prints it out.
# Answers should be given as yes/no

# Required libraries: random, string

import random, string

def generate_password(length, uppercase, numbers, special_chars):
    # Define the characters that can be used in the password
    chars = string.ascii_lowercase
    if uppercase:
        chars += string.ascii_uppercase
    if numbers:
        chars += string.digits
    if special_chars:
        chars += string.punctuation

    # Generate the password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Get user input
length = int(input("Enter the desired password length: "))
uppercase = input("Do you want to include uppercase letters? (yes/no): ").lower() == "yes"
numbers = input("Do you want to include numbers? (yes/no): ").lower() == "yes"
special_chars = input("Do you want to include special characters? (yes/no): ").lower() == "yes"

# Generate and print the password
password = generate_password(length, uppercase, numbers, special_chars)
print(f"Generated password: {password}")


# Time started: 5:58 PM
# Time finished: 6:00 PM
# With assistance of Github Copilot
