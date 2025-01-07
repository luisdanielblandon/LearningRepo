# Started 11:51AM

numbers = [3, 1, 2, 3, 4, 1, 5, 2]

cleanednumbers = []

for number in numbers:
      if number not in cleanednumbers:
            cleanednumbers.append(number)

print(f"The list of numbers before cleaning is:{numbers}\n\n")
print(f"The final list without dupes is:{cleanednumbers}\n")

# Finished 12:00PM