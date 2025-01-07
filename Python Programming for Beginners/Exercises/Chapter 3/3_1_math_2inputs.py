print("Welcome to our little math program.")
Value1 = int (input("\nPlease provide the first input (integers only, please.)\n"))
Value2 = int (input("\nPlease provide the second input (integers only, please.)\n"))

print("\nCalculating...\n")

print("Multiplication Result:")
print(Value1 * Value2,"\n")

print("Division Result:")
print(Value1 / Value2,"\n")

print("Floor Division Result:")
print(Value1 // Value2,"\n")

print("Modulus Result:")
print(Value1 % Value2,"\n")

print("Addition Result:")
print(Value1 + Value2,"\n")

print("Subtraction Result:")
print(Value1 - Value2,"\n")

print("Square Result:")
i = 0
for x in range(0,Value2):
      if i==0:
            SquaredResult = Value1 * Value1
      else:
            SquaredResult = SquaredResult * Value1
      i = i+1
print(SquaredResult,"\n")