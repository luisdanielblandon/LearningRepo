class BankAccount:
      def __init__(self, name, balance, accounttype):
            self.name = name
            self.balance = balance
            self.accounttype = accounttype

      def get_balance(self):
            return self.balance
      
      def make_deposit(self, transactionamount):
            self.balance = self.balance + transactionamount
            return self.balance
      
      def make_withdrawal(self, transactionamount):
            self.balance = self.balance - transactionamount
            return self.balance
      
account01 = BankAccount('Chris',5000.00,'Checking')

print("You have created an account:"+account01.name,account01.accounttype,account01.balance)

print("Now we make a deposit for $2500.00\n")

account01.make_deposit(2500.00)

print(account01.balance)

print("Now we make a withdrawal for $6200.00")

account01.make_withdrawal(6200.00)

print(account01.balance)