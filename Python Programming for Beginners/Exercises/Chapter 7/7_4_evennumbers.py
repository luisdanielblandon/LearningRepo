UserInput = int(input("How many even numbers would you like to see? Starting at 0. (Integers only)"))

for number in range(1,UserInput):
      if int(number) % 2 == 0:
            print(number)
