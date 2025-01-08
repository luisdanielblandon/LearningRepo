# The program starts by prompting the user to enter some text in the
# terminal: The user pastes some text. 
# After the user presses Enter, they get different statistics about the
# submitted text: the number of words, sentences, and characters, the
# most frequent words used in the text, the average word length, and
# the average sentence length.

# 1. Accept user input
# 2. Separate into sentences
# 3. Separate into words
# 4. Count words, sentences, characters
# 5. Find most frequent words
# 6. Calculate average word length
# 7. Calculate average sentence length

import string

user_input = input("Please enter some text: ")

# 2. Separate into sentences
sentences = user_input.split(".") #I also need to check for exclamation points and question marks on the next line
sentences = [sentence.split("!") for sentence in sentences]
sentences = [sentence for sublist in sentences for sentence in sublist]
sentences = [sentence.split("?") for sentence in sentences]
sentences = [sentence for sublist in sentences for sentence in sublist]
sentences = [sentence for sentence in sentences if sentence]

# 3. Separate into words
words = user_input.split()
words = [word.strip(string.punctuation) for word in words]  # Remove punctuation
words = [word for word in words if word]

# 4. Count words, sentences, characters
num_words = len(words)
num_sentences = len(sentences)
num_characters = len(user_input)
num_characters_without_special = len(user_input) - user_input.count(" ") - user_input.count(".") - user_input.count(",") - user_input.count("!") - user_input.count("?")

# 5. Find most frequent words
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
most_frequent_words = [word for word, freq in word_freq.items() if freq == max(word_freq.values())]

# 6. Calculate average word length
average_word_length = sum(len(word) for word in words) / num_words

# 7. Calculate average sentence length
average_sentence_length = num_words / num_sentences # in number of words
average_sentence_length_allcharacters = num_characters / num_sentences # including special characters
average_sentence_length_characters = num_characters_without_special / num_sentences # without special characters

print("\nHere's an analysis of the text you provided:\n\n")
print(f"Number of words: {num_words}\n")
print(f"Number of sentences: {num_sentences}\n")
print(f"Number of characters: {num_characters}\n")
print(f"Number of characters (excluding punctuation and whitespace): {num_characters_without_special}\n")
print(f"Most frequent word(s): {', '.join(most_frequent_words)}\n")
print(f"Average word length: {average_word_length}\n")
print(f"Average sentence length (# of words): {average_sentence_length}\n")
print(f"Average sentence length (# of characters): {average_sentence_length_allcharacters}\n")
print(f"Average sentence length (# of characters, excluding special): {average_sentence_length_characters}\n")
print("\nThank you! Goodbye!!\n")

# Tested with the following text (and sample results):
# My father was thistle sifter. He sifted thistles, until the sifted thistles could be thistled
# and sifted no more! Only then, was he truly satisfied. A man, so blinded by rage. Poop.
# 
# Here's an analysis of the text you provided:
# 
# 
# Number of words: 32
# 
# Number of sentences: 5
# 
# Number of characters: 181
# 
# Number of characters (excluding punctuation and whitespace): 142
# 
# Most frequent word(s): sifted
# 
# Average word length: 4.4375
# 
# Average sentence length (# of words): 6.4
# 
# Average sentence length (# of characters): 36.2
# 
# Average sentence length (# of characters, excluding special): 28.4


# Started at: 5:30 PM

# Finished at 5:45 PM