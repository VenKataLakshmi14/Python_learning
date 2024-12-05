class BankAccount:
    def __init__(self, owner, account_type="Saving", balance=0):
        self.owner = owner 
        self.account_type = account_type  
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

# Create an instance of the BankAccount class
account1 = BankAccount("ganesh")


print(account1.owner)        
print(account1.account_type)

# Modifying public attributes
account1.account_type = "Checking"

# Deposit money
account1.deposit(100)

# Withdraw money
account1.withdraw(50)

# Check balance
print(account1.get_balance()) 
account1.deposit(200)
account1.withdraw(100) 
print(account1.get_balance()) 



