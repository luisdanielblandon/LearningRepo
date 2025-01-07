def sum(a,b):
      c = a + b
      return c

print("Let me do some math for you. I'll sum two numbers. It's really cool.\n")

print("And here's the sum!\n" + str(sum(int(input("What's the first number?\n")), int(input("What's the second number?\n")))))

'''
This is the ugliest code I could manage to make.
I could split it into multiple lines, and assign the
result of the sum function into a global variable,
but instead I saved one microsopic step by not returning
to local variable c and reassigning the value to a
global variable. I think.
'''