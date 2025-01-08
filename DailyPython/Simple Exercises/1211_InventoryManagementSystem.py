# Build a command-line app that allows a small business to manage their
# inventory. The app will let users:
#     add new item (including name, price, and quantity)
#     update stock
#     view all items
#     search for specific items by name
# 
# This project is perfect for practicing CRUD (Create, Read, Update, Delete)
# operations using dictionaries.

# Required libraries: string

# Create an empty dictionary to store the inventory items
inventory = {}

# Create a loop to display the menu and get user input
while True:
      print("\nInventory Management System")
      print("1. Add New Item")
      print("2. Update Stock")
      print("3. View All Items")
      print("4. Search for Item")
      print("5. Exit")
      
      choice = input("Enter your choice: ")
      
      if choice == "1":
            # Add a new item to the inventory
            name = input("Enter the item name: ")
            price = float(input("Enter the price: "))
            quantity = int(input("Enter the quantity: "))
            
            inventory[name] = {"price": price, "quantity": quantity}
            print(f"{name} added to inventory.")
            
      elif choice == "2":
            # Update the stock of an existing item
            print("\nCurrent Inventory:")
            print("No.\tItem\t\tPrice\tQuantity")
            items = list(inventory.items())
            for i, (name, details) in enumerate(items, start=1):
                  print(f"{i}\t{name}\t\t${details['price']}\t{details['quantity']}")
            
            item_number = int(input("Enter the item number: "))
            if 1 <= item_number <= len(items):
                  name = items[item_number - 1][0]
                  quantity = int(input("Enter the new quantity: "))
                  inventory[name]["quantity"] = quantity
                  print(f"{name} stock updated.")
            else:
                  print("Invalid item number.")
                  
      elif choice == "3":
            # View all items in the inventory
            print("\nCurrent Inventory:")
            print("No.\tItem\t\tPrice\tQuantity")
            for i, (name, details) in enumerate(inventory.items(), start=1):
                  print(f"{i}\t{name}\t\t${details['price']}\t{details['quantity']}")
                  
      elif choice == "4":
            # Search for a specific item by name
            name = input("Enter the item name: ")
            if name in inventory:
                  details = inventory[name]
                  print("\nItem Details:")
                  print("Item\t\tPrice\tQuantity")
                  print(f"{name}\t\t${details['price']}\t{details['quantity']}")
            else:
                  print(f"{name} not found in inventory.")
                  
      elif choice == "5":
            print("Thank you for using my app!")
            break
            
      else:
            print("Invalid choice. Please try again.")
            
# Started 6:12 PM
# Finished 6:22 PM
# With assistance from Github Copilot