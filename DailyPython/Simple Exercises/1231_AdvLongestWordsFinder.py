# Allows the user to input a list of words in the terminal and let them 
# specify the minimum word
# Identifies the longest word(s) in the list, including multiple words with
# the same maximum length and prints out a message that includes the number
# of characters of that word.
# User input takes the form of one line "word1 word2 word3"

user_input = input("Please enter the words you would like considered with spaces inbetween.")

words = user_input.split(" ")
maxlen = 0

for word in words:
      if len(word) >= maxlen:
            maxlen = len(word)
            longestword = word
            
print(longestword)

# Started 6:40 PM
# Finished 6:45 PM
# No assistance or google! Yay!