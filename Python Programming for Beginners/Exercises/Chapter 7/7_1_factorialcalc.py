UserInput = int(input("What number would you like to factorialize? (Integers only)"))

FactorialTotal = UserInput
FactorialBase = UserInput

for numbers in range(1,UserInput):
      FactorialTotal = FactorialTotal * (FactorialBase - 1)
      FactorialBase = FactorialBase - 1

print("The factorial of",UserInput," is:",FactorialTotal)