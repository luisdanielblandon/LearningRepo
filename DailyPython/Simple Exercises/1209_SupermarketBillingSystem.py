# Create a command line program that simulates a basic billing system
# for a supermarket. The user can input items purchased (e.g., butter,
# eggs, etc), their prices, and quantities. The app will calculate the
# total bill, apply any applicable discounts, and display an itemized
# bill summary. This project focuses on loops, dictionaries, and
# arithmetic calculations.

# Required libraries: None

# Begin with user input where the user can add items to the cart (with prices and quantities)
# Once the user confirms they're finished (by entering "Done" as the item name)
# Then, calculate the total bill and apply any discounts
# Finally, display the itemized bill summary

# Create an empty dictionary to store the items and their prices
items = {}

# Create a loop to add items to the cart
while True:
    # Get the item name, price, and quantity from the user
    item = input("Enter the item name: ")
    if item.lower() == "done":
        break
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
    
    # Store the item and its price in the dictionary
    items[item] = {"price": price, "quantity": quantity}
    
# Calculate the total bill
total = 0
for item, details in items.items():
    total += details["price"] * details["quantity"]
    
# Apply a discount if the total bill is over $100
if total > 100:
    total *= 0.9  # 10% discount
    
# Display the itemized bill summary
print("\nItemized Bill Summary:")
print("Item\t\tPrice\tQuantity\tTotal")
for item, details in items.items():
    print(f"{item}\t\t${details['price']}\t{details['quantity']}\t\t${details['price'] * details['quantity']}")
# Print the value of the applied discount. If no discount applied, print nothing.
if total > 100:
      print("\n10% discount applied.")

    
print(f"\nTotal Bill: ${total}")

# Time started: 6:02 PM
# Time finished: 6:08 PM

# Issues with text alignment when the item names are different by about 4 characters (length of a tab)