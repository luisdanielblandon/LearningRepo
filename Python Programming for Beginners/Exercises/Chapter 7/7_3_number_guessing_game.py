import random

RandomNumber = random.randint(1,100)

UserInput = 0

while UserInput != RandomNumber:
      UserInput = int(input("How many bits am I holding behind my motherboard? (1-100)\n"))

      if UserInput > RandomNumber:
            print("\nToo high! Try again...\n")
            continue
      if UserInput < RandomNumber:
            print("\nToo low! Keep trying...\n")

if UserInput == RandomNumber:
      print("\nWowzers, you're so smart I should just lock you in a dungeon so you can do things for me all day.\n")
