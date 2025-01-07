#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:50:32 2019

@author: Giles
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''

userint1 = int(input("Please provide the first integer: 1-100"))
userint2 = int(input("Please provide the second integer: 1-100"))

if userint1 < userint2:
      for i in range(userint1,userint2+1):
            print(i)
elif userint1 >= userint2:
      print("The first integer is bigger than the second! I can't show you my magic trick.")

'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''

userinput = input("Type aaaannnyyy sentence you want.")

for i in reversed(userinput):
      print(i)


'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''

userint1 = int(input("What is the integer you would like a simple times table for?"))

for x in range(1,10):
     print(userint1, "x", x, "=", userint1 * x)

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''

for x in range(1,13):
      for y in range(1, 13):
          print(x, "x", y, "=", x * y)


'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''

userinput = list(map(int, input("Please provide integers for the sequence. Separate with whitespace ' ' and press enter when done.").split()))

print("The sum of all integers provided is:", sum(userinput), "and the average is:", (sum(userinput) / len(userinput)))


'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''

userint1 = 1

for x in range(1,16):
      userint1 = userint1 * x
      print(userint1)
print("That was a 15 factorial.")


userint1 = int(input("Enter an integer to factorialize:"))
userint2 = 1

for x in range(1,userint1+1):
      userint2 = userint2 * x
      print(userint2)

#for x in range(1,userint1):
#    userint1 = userint1 * x
#     print(userint1)

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''

userint1 = 1
userint2 = 1

for x in range(0,19):
     if x == 0:
          print("0")
     elif x == 1:
          print(userint1)
     else:
          userint2, userint1 = userint2 + userint1, userint2
          print(userint2)


'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''

print("*****\n*\n****\n*\n*\n*")


'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''

def isEven(number):
     if number % 2 == 0:
          return True
     else:
          return False

evenlist = []
oddlist = []

for x in range (1,100+1):
     if isEven(x):
          evenlist.append(x)
     else:
          oddlist.append(x)

print("All Even Numbers:", evenlist)
print("All Odd Numbers:", oddlist)