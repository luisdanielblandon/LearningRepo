#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:04:18 2019

@author: Giles
"""

'''
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
'''

userinput = int(input("Enter a number between one and five, as an integer."))

if userinput == 1:
      print("One.")
elif userinput == 2:
      print("Two.")
elif userinput == 3:
      print("Three.")
elif userinput == 4:
      print("Four.")
elif userinput == 5:
      print("Five.")

'''
Question 2
Repeat the previous task but this time the user will input a string and the
code will ouput the integer value. Convert the string to lowercase first.
'''

userinput = input("Enter a number between one and five, using the full word.")
userinput = userinput.lower()

if userinput == 'one':
      print("1")
elif userinput == 'two':
      print("2")
elif userinput == 'three':
      print("3")
elif userinput == 'four':
      print("4")
elif userinput == 'five':
      print("5")

'''
Question 3
Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.
'''

randomnumber = 5
userinput = int(input("Guess the secret number. Between 1-15."))

if userinput == 5:
      print("You got it!")
else:
      print("Uh-uh-uh, you didn't say the magic word. (Newman face)")

'''
Question 4
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
'''

username = input("Please enter your name.")

if len(username) >= 15:
      print("Ohhhh look at that long name. It has", len(username), "characters!")
else:
      print("Look at that witto namey-wamey.")

'''
Question 5
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
'''
userint1 = int(input("Please provide the first integer (any positive number)"))
userint2 = int(input("Please provide the second integer (any positive number)"))

if userint1 >= 15 and userint2 >= 15:
      print("The result of", userint1, "*", userint2, "is:\n", (userint1 * userint2))
elif userint1 >= 15 or userint2 >= 15:
      print("The result of", userint1, "+", userint2, "is:\n", (userint1 + userint2))
else:
      print("Both numbers are less than 15, so the answer is 0.")

'''
Question 6
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
'''

var_1 = int(input("Please provide the first integer."))
var_2 = int(input("Please provide the second integer."))

print("I will now switch var_1 =", var_1, "with var_2 =", var_2)

var_1, var_2 = var_2, var_1

print("Kooloolimpaaa! var_1 =", var_1, "and var_2 =", var_2)