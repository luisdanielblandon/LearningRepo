#Started at 5:33 PM

quiz_questions = [
    ("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2),
    ("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3),
    ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], 1),
]


def print_nested_tuple(t):
    for item in t:
        if isinstance(item, tuple):  # Check if the item is a tuple
            print_nested_tuple(item)  # Recursively print the nested tuple
        else:
            print(item)


score = 0
iterator = 0

for question in quiz_questions:
      print(f"{quiz_questions[int(iterator)][0]}\n")

      for choices in quiz_questions[iterator][1]:
            print(f"{choices}\n")
      
      user_input = str(input("Which answer do you choose (1, 2, 3, or 4)?"))

      if int(user_input) == int(quiz_questions[iterator][2]):
            print("\nYou got it!!\n\n")
            score = score + 1
      else:
            print("\nWRONG! No points for you. Next question.\n\n")

      iterator = iterator + 1


print(f"Good job on the quiz! Your final score is {score}")

#Finished at 6:01PM