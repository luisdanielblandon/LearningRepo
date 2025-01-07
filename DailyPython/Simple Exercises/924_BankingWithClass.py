# Started 12:02 PM

def askforname():
      name = input("Enter the account owner's name: ")
      return name

class BankAccount:
      def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance

      def deposit(self, amount):
            self.balance += amount
            return self.balance

      def withdraw(self, amount):
            if amount > self.balance:
                  return "Insufficient funds"
            else:
                  self.balance -= amount
                  return self.balance

      def __str__(self):
            return f"BankAccount(owner: {self.owner}, balance: {self.balance})"

accounts = {}

while True:
      print("\nChoose an action:")
      print("1. Create account")
      print("2. Deposit")
      print("3. Withdraw")
      print("4. Check balance")
      print("5. Exit")
      
      action = int(input("Enter the number of the action you want to perform: "))

      if action == 1:
            name = askforname()
            balance = float(input("Enter the initial balance: "))
            accounts[name] = BankAccount(name, balance)
            print(f"Account created for {name}: {accounts[name]}")
      elif action == 2:
            name = askforname()
            if name in accounts:
                  amount = float(input("Enter the amount to deposit: "))
                  print(f"New balance for {name}: {accounts[name].deposit(amount)}")
            else:
                  print(f"No account found for {name}")
      elif action == 3:
            name = askforname()
            if name in accounts:
                  amount = float(input("Enter the amount to withdraw: "))
                  print(f"New balance for {name}: {accounts[name].withdraw(amount)}")
            else:
                  print(f"No account found for {name}")
      elif action == 4:
            name = askforname()
            if name in accounts:
                  print(f"Current balance for {name}: {accounts[name].balance}")
            else:
                  print(f"No account found for {name}")
      elif action == 5:
            confirm = input("Are you sure you want to exit? (yes/no): ")
            if confirm.lower() == 'yes':
                  print("Exiting...")
                  break
      else:
            print("Invalid action. Please choose a valid option.")

# Finished at 12:15 PM with help from Copilot

# Issue 1: Linting errors due to repetitive input() calls asking for the name.
# Fix: A function was defined (askforname) to handle the input() calls

# Issue 2: Using a string instead of integers for actions causes crashes.