ColorPalette = ['Red','Blue','Green']

print("There's a list of colors. Can you guess 1 of the 3?")

UserColor = input()

if (UserColor in ColorPalette) == True:
      print("What a good little guesser you are.")
else:
      print("Oh no! That's OK, though. Here's the new list, with your color added!")
      ColorPalette.append(UserColor)
      print(ColorPalette)
      print("\nThere are no mistakes. Only happy accidents.")

'''
Lesson learned: if statement (variable IN variable) must be within parantheses or it fails to check with no error
'''