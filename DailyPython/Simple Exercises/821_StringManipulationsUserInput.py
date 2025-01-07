def reverse(string):
    string = string[::-1]
    return string

userinput = input("What is your full name? First and last please.")

print("You said your name is:", userinput)
print("Your name in uppercase is:" + str.upper(userinput))
print("Your name in lowercase is:" + str.lower(userinput))
print("The total number of characters (excluding spaces) is:" + str(len(userinput) - userinput.count(' ')))
print("Your name in reverse is:" + reverse(userinput))