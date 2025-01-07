import os

#Determine the python script's file path, parent directory, and set
#file_path to the new bilingual_dict to be created/amended.
file_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_path, '826_saved_bilingual_dict.txt')

#Create two empty lists to store the words and their translations.
words = []
translations = []


#Ask the user for the names of the two languages to be used in the bilingual dictionary.
languagename1 = str(input("Please provide the name of the first language:\n"))
languagename2 = str(input("Please provide the name of the second language:\n"))


#Set the iterators for the while loop and the input_string.
input_string = "start"
iterator = 0

#Iterate through the while loop, asking the user for the base word and translation.
#Inputting "done" breaks the loop.
while input_string != 'done':
      input_string = str(input(f"Please provide the base word in {languagename1}:\n"))
      if input_string == 'done':
            break
      words.append(input_string)
      input_string = str(input(f"Please provide the translation for the word in {languagename1}:\n"))
      if input_string == 'done':
            break
      translations.append(input_string)
      
#Create a dictionary from the two lists, defining the key as "word" and the value as "translation".
bilingual_dict = {word: translation for word, translation in zip(words, translations)}


#Write the contents of bilingual_dict to the TXT file at file_path, based on an expected template.
with open(file_path, "a") as file:
      file.write(languagename1 + " -- " + languagename2 + "\n")
      for each in bilingual_dict:
            file.write(each + " -- " + bilingual_dict[each] + "\n")
      file.write("---------\n")