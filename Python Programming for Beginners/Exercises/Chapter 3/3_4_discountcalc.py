OriginalPrice = float(input("What is the original price of the item?"))
DiscountAmount = float(input("And what is the discount percentage to be applied?"))

print("\nThe original price is: $",OriginalPrice)
print("The discount percentage is:",DiscountAmount,"%")
print("The total discount is: $",OriginalPrice*(DiscountAmount / 100))
print("The final price is: $",OriginalPrice-(OriginalPrice*(DiscountAmount / 100)))

'''
TODO:
- Two digits in output
- Error-checking for non-numbers
- GUI
'''