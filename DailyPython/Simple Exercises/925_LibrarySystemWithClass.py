class LibraryBook:
      def __init__(self, title, author, checkout = 0):
            self.title = title
            self.author = author
            self.checkout = checkout

      def borrowbook(self, title): #Finish updating this function
            if title in librarybooks:
                  if self.checkout == 0:
                        self.checkout = 1
                        print ("You have checked out {title}. Remember to bring it back on time!\n")
                        return self
                  if self.checkout == 1:
                        print("This book is already checked out. Sorry!\n")

      def returnbook(self, title): #Update function to match borrowbook
            if title in librarybooks:
                  if title.checkout == 1:
                        title.checkout = 0
                        print(f"Thank you for returning {title}!\n")
                        return self
                  if title.checkout == 0:
                        print("This book is not checked out.\n")
            else:
                  print("We don't have that book in our library.\n")

      def __str__(self):
            return f"{self.title} by {self.author}"

librarybooks = {}

# Class created, need to update the functions to properly search for the required book
# Copy over user input and output logic from BankingWithClass.py