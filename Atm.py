class ATM:
    def __init__(self, balance=0, account_number=None, pin=None):
        self.balance = balance
        self.account_number = account_number
        self.pin = pin
        self.transaction_history = []
        self.is_authenticated = False

    def create_account(self):
        self.account_number = input("Enter your account number: ")
        self.pin = input("Enter your PIN: ")
        print("Account created successfully!")

    def authenticate(self, account_number, pin):
        if account_number == self.account_number and pin == self.pin:
            self.is_authenticated = True
            print("Authentication successful. You are now logged in.")
        else:
            print("Invalid account number or PIN. Please try again.")

    def display_balance(self):
        if self.is_authenticated:
            print(f"Your account balance: ${self.balance:.2f}")
        else:
            print("Please authenticate first.")

    def deposit(self, amount):
        if self.is_authenticated:
            if amount > 0:
                self.balance += amount
                self.transaction_history.append(f"Deposited ${amount:.2f}")
                print(f"Deposited ${amount:.2f}")
            else:
                print("Invalid amount for deposit.")
        else:
            print("Please authenticate first.")

    def withdraw(self, amount):
        if self.is_authenticated:
            if 0 < amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdraw ${amount:.2f}")
                print(f"Withdrew ${amount:.2f}")
            else:
                print("Invalid amount for withdrawal or insufficient funds.")
        else:
            print("Please authenticate first.")

    def transfer(self, amount, recipient):
        if self.is_authenticated:
            if 0 < amount <= self.balance:
                self.balance -= amount
                recipient.balance += amount
                self.transaction_history.append(f"Transferred ${amount:.2f} to {recipient.account_number}")
                print(f"Transferred ${amount:.2f} to {recipient.account_number}")
            else:
                print("Invalid amount for transfer or insufficient funds in your account.")
        else:
            print("Please authenticate first.")

    def show_transaction_history(self):
        if self.is_authenticated:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("Please authenticate first.")

def main():
    account1 = ATM()
    account2 = ATM()

    while True:
        print("\nOptions:")
        print("1. Create Account")
        print("2. Authenticate")
        print("3. Display Balance")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer")
        print("7. Transaction History")
        print("8. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            account1.create_account()
        elif choice == '2':
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")
            account1.authenticate(account_number, pin)
        elif choice == '3':
            account1.display_balance()
        elif choice == '4':
            amount = float(input("Enter the deposit amount: $"))
            account1.deposit(amount)
        elif choice == '5':
            amount = float(input("Enter the withdrawal amount: $"))
            account1.withdraw(amount)
        elif choice == '6':
            amount = float(input("Enter the transfer amount: $"))
            account1.transfer(amount, account2)
        elif choice == '7':
            account1.show_transaction_history()
        elif choice == '8':
            print("Thank you for using our ATM. Have a good day ahead!")
            break
        else:
            print("Invalid option selected. Please select a valid option.")

if __name__ == "__main__":
    main()











'''class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    def display_balance(self):
        print(f"Your account balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount:.2f}")
            print(f"Deposited ${amount:.2f}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Invalid amount for withdrawal or insufficient funds.")

    def transfer(self, amount, recipient):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount:.2f} to {recipient}")
            print(f"Transferred ${amount:.2f} to {recipient}")
        else:
            print("Invalid amount for transfer or insufficient funds in your account.")

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

def main():
    account1 = ATM()
    account2 = ATM()

    while True:
        print("\nOptions:")
        print("1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            account1.display_balance()
        elif choice == '2':
            amount = float(input("Enter the deposit amount: $"))
            account1.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the withdrawal amount: $"))
            account1.withdraw(amount)
        elif choice == '4':
            amount = float(input("Enter the transfer amount: $"))
            account1.transfer(amount, account2)
        elif choice == '5':
            account1.show_transaction_history()
        elif choice == '6':
            print("Thank you for using our ATM. Have a good day ahead!")
            break
        else:
            print("Invalid option selected. Please select a valid option.")

if __name__ == "__main__":
    main()'''