# Add some code that combines the two lists into one single list.
# Removes any duplicates from the combined list.
# Sort the combined list in ascending order.
# Print out the sorted list.

list1 = [5, 3, 8, 6, 3]
list2 = [7, 2, 5, 9, 8]

print(list1,'\n')
print(list2,'\n')

# Combine list1 and list2 while removing duplicates
combined = list1 + list2
print(combined)

cleanlist = []

for number in combined:
      if number not in cleanlist:
            cleanlist.append(number)
            
cleanlist.sort()

print("The combined and cleaned list of numbers is:\n")
print(cleanlist)

# Started 6:25 PM
# Finished 6:35 PM