# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:32:12 2019

@author: giles
"""

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''

capitals = {'United States':'Washington, DC','France':'Paris','Canada':'Alberta'}

userinput1 = input("Which country would you like the capital for?")

if userinput1 in capitals:
      print(capitals[userinput1])


'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''

userdict = {}
xfib = 1
xfibold = 0

for xindex in range(1,12):
      if xindex == 1:
            userdict[xindex] = 0
      elif xindex == 2:
            userdict[xindex] = xfib
      elif xindex > 2:
            userdict[xindex], xfibold, xfib = xfib + xfibold, xfib, xfib + xfibold

print(userdict)


'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''

StockPrices = {'PythonDS':{'Open':12.87,'High':13.23,'Low':11.42,'Close':13.10},'PythonSoft':{'Open':23.54,'High':25.76,'Low':21.87,'Close':22.33},'Pythazon':{'Open':98.99,'High':102.34,'Low':97.21,'Close':100.065},'Pybook':{'Open':203.63,'High':207.54,'Low':202.43,'Close':205.24}}

userinput1 = input("Which company would you like stock prices for?")

if userinput1 in StockPrices:
      print("The company is:",userinput1)
      print("Open:",StockPrices[userinput1]['Open'])
      print("High:",StockPrices[userinput1]['High'])
      print("Low:",StockPrices[userinput1]['Low'])
      print("Close:",StockPrices[userinput1]['Close'])

'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''


'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''

import random
import matplotlib.pyplot as plt

userdict = {}

for x in range(ord('A'),ord('Z')+1):
      userdict[chr(x)] = random.randint(1,100)

print(userdict)

plt.bar(userdict.keys(), userdict.values())
plt.show()


'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''

userdict = {'Spades':('Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'),'Clubs':('Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'),'Hearts':('Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'),'Diamonds':('Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King')}

for x, y in userdict.items():
      print(y,"of",x)
      