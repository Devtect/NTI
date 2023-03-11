'''
Suppose you want to create a class called Rectangle that represents a rectangle. Each rectangle should have the following attributes:

width: a float representing the width of the rectangle.
height: a float representing the height of the rectangle.

In addition to these attributes, the Rectangle class should have the following method:

get_area(): calculates and returns the area of the rectangle. (Calculation for the area is: width * height)

'''
class BankAccount:
    def __init__ (self, owner, balance):
        self.owner = str(owner)
        self.balance = float(balance)
        
    def deposit(self):
        depo = float(input("how much?"))
        self.balance += depo
    def withdraw(self):
        withdr = int(input("How much?"))
        withdr -= self.balance
    def __str__(self):
        return f"Balance: {self.balance} Account owner: {self.owner}"

customer1 = BankAccount("Jason", 0)

menu = input("please select and operation: 1-deposit  2-withdraw")
if menu == "1":
    customer1.deposit()
    print(customer1)
elif menu == "2":
    customer1.withdraw()