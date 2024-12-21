UserInput = input("Please type any text you'd like, and I'll count the number of vowels (NOT Y!)")

VowelCount = 0

for letter in UserInput:
      if letter == 'a':
            VowelCount += 1
      if letter == 'e':
            VowelCount += 1
      if letter == 'i':
            VowelCount += 1
      if letter == 'o':
            VowelCount += 1
      if letter == 'u':
            VowelCount += 1
      if letter == 'A':
            VowelCount += 1
      if letter == 'E':
            VowelCount += 1
      if letter == 'I':
            VowelCount += 1
      if letter == 'O':
            VowelCount += 1
      if letter == 'U':
            VowelCount += 1

print("In your provided string, there are",VowelCount,"vowels. Pretty neat, huh?")