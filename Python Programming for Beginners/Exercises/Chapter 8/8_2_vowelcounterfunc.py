def count_vowels(user_input):
      vowel_count = 0

      for letter in str.lower(user_input): # converts string to lowercase then checks for vowels
            if letter == 'a':
                  vowel_count += 1
            if letter == 'e':
                  vowel_count += 1
            if letter == 'i':
                  vowel_count += 1
            if letter == 'o':
                  vowel_count += 1
            if letter == 'u':
                  vowel_count += 1

      return vowel_count

user_input = input("Please type any text you'd like, and I'll count the number of vowels (NOT Y!)")

num_vowels = str(count_vowels(user_input))

print("In your provided string, there are", num_vowels, "vowels. Pretty neat, huh?")