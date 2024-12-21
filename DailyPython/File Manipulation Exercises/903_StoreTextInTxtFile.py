userinput = input("Please enter the first line of text to be saved:")

while len(userinput) != 0:
    with open("savedlines.txt", "a") as file:
      file.write(userinput + "\n")
      file.write("---------\n")
    userinput = input("Please enter the next line of text to be saved:")