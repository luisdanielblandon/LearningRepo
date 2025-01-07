UserInput = int(input("How many numbers in the Fibonacci Sequence do you want to generate? (Integers only)"))

FibNumber1 = 0
FibNumber2 = 1
FibTemp = 0

for x in range(0,UserInput):
      if x == 0:
            print(FibNumber1)
      if x == 1:
            print(FibNumber2)
      else:
            FibTemp = FibNumber2
            FibNumber2 = FibNumber1 + FibNumber2
            FibNumber1 = FibTemp
            print(FibNumber2)

