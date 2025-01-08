# User enters a list of ingredients they have available,
# Once the user enters the ingredients, they will get all
# the recipes that can be cooked using those ingredients.
# For example, since the user had bread, salt, and oil, the
# oil bruschetta recipe showed up since it was the recipe in
# the JSON file that had can be made with the ingredients that the user had.

# Required libraries: json

# Associated files:
# LearningRepo/DailyPython/Simple%20Exercises/1104_recipes.json

import json, os

# Load the recipes from the JSON file. Use the OS library to get the directory with 1104_recipes.json
# and open the file in read mode.
with open(os.path.join(os.path.dirname(__file__), "1104_recipes.json"), "r") as file:
    recipes = json.load(file)
    
# Get the user's input for the ingredients they have available.
user_ingredients = input("Enter the ingredients you have available, separated by commas: ").split(",")
# I need to add a line that strips any whitespace from the user's input.
user_ingredients = [ingredient.strip(" ") for ingredient in user_ingredients]

# Create a list to store the recipes that can be made with the user's ingredients.
possible_recipes = []

# Loop through each recipe in the recipes dictionary.

for recipe in recipes:
      print(f"Checking recipe: {recipe['name']}")
      print(f"Checking recipe: {recipe['ingredients']}")
      for ingredient in user_ingredients:
            print(f"Checking ingredient: {ingredient}")
            
            # Check if all the ingredients in the recipe are in the user's ingredients.
      if all(ingredient in recipe['ingredients'] for ingredient in user_ingredients):
            # If all the user's ingredients are in the recipe's ingredients, add the recipe to the possible_recipes list.
            possible_recipes.append(recipe['name'])
            print("Prove LOOP")
        
# Print the recipes that can be made with the user's ingredients.

if possible_recipes:
      print("You can make the following recipes with the ingredients you have available:")
      for recipe in possible_recipes:
            print(recipe)
else:
      print("No recipes can be made with the ingredients you have available.")


# Started at 3:00 AM
# Finished at 3:46 AM

# Trapped in a debugging nightmare. If function was not working because Copilot
# autocompleted the function in reverse. Read the doc and chatted with Copilot
# on how all() works and recognized the error. Tested with ingredient "butter" and "garlic"