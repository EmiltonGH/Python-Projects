class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance # Start with an initial balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited £{amount}. New balance is £{self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew £{amount}. New balance is £{self.balance}.")
        else:
            print("Sorry!,insufficient funds.")

    def display_balance(self):
        print(f"Current balance: £{self.balance}")

# Creating an instance of BankAccount class
account = BankAccount("56765438", "Emilton", 100)
account.deposit(50)
account.withdraw(30)
account.display_balance()
account.withdraw(170)