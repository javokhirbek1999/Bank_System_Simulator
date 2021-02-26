from random import randint


class Banking:
    def __init__(self):
        self.savings_account = {}
        self.already_authenticated = False

    def create_account(self):
        self.name = str(input("Enter your name: "))
        self.account_number = randint(1000000, 9999999)
        initial_deposit = input("Enter the initial deposit:")
        self.savings_account[self.account_number] = [self.name, int(initial_deposit)]
        print(f"Account {self.name} has been created successfully\nYour account number is ", self.account_number)
        self.main_menu()

    def show_balance(self):
        print(f"Name: {self.savings_account.get(self.account_number)[0]}"
              f"\nBalance: ${self.savings_account.get(self.account_number)[1]}"
              f"\nAccount: {self.account_number}\n")
        self.login()

    def authenticate(self, name):
        for i in self.savings_account.keys():
            if self.savings_account.get(i)[0] == name:
                print("Account Found")
                account_num = int(input("Enter your account number: "))
                if self.savings_account.get(account_num):
                    self.account_number = account_num
                    print("Authentication successful")
                    self.already_authenticated = True
                    self.login()
                    # return True
                else:
                    print("Authentication failed. Invalid Account Number")
                    self.already_authenticated = False
                    self.main_menu()
                    # return False
            else:
                print("Sorry, there is no account with such name")
                self.already_authenticated = False
                self.main_menu()
                # return False

    def withdraw(self):
        print("Enter -1 to go back: ")
        amount_to_withdraw = int(input("Enter the amount to withdraw: "))
        if amount_to_withdraw == -1:
            self.login()
        if amount_to_withdraw >= self.savings_account.get(self.account_number)[1]:
            print("Insufficient funds to withdraw")
            self.withdraw()
        else:
            userChoice = int(input(f"Are you sure to withdraw ${amount_to_withdraw}?\n1.\tYes\n2.\tNo\n>"))
            if userChoice == 1:
                self.savings_account.get(self.account_number)[1] -= amount_to_withdraw
                print(f"${amount_to_withdraw} has been successfully withdrew from account number {self.account_number}")
                self.show_balance()
            else:
                print(f"Available options: \n1.\tWithdraw\n2.\tGo Back")
                choice = int(input("> "))
                if choice == 1:
                    self.withdraw()
                else:
                    self.main_menu()

    def login(self):
        if not self.already_authenticated:
            name = input("Enter your name: ")
            self.authenticate(name)
        else:
            if self.already_authenticated:
                print(f"\nAvailable Options: "
                      f"\n1.\tWithdraw"
                      f"\n2.\tDeposit"
                      f"\n3.\tShow Balance"
                      f"\n4.\tGo Back"
                      f"\n5.\tExit")
                userChoice = int(input("> "))
                if userChoice == 1:
                    self.withdraw()
                if userChoice == 2:
                    self.deposit()
                if userChoice == 3:
                    self.show_balance()
                if userChoice == 4:
                    self.main_menu()
                if userChoice == 5:
                    quit()
                else:
                    self.login()

    def deposit(self):
        print("Enter -1 to go back: ")
        amount_to_deposit = int(input("Enter the amount to deposit: "))
        if amount_to_deposit == -1:
            self.login()
        choice = int(input(f"Are you sure to deposit ${amount_to_deposit}\n1.\tYes\n2.\tNo\n"))
        if choice == 1:
            self.savings_account.get(self.account_number)[1] += amount_to_deposit
            print(f"${amount_to_deposit} has been deposited successfully into the account {self.account_number}\n")
            self.login()
        else:
            self.deposit()

    def main_menu(self):
        user_choice = int(input("Main menu: \n1.\tCreate a new account\n2.\tLogin an existing account\n3.\tExit\n>"))
        if user_choice == 1:
            self.create_account()
        if user_choice == 2:
            self.login()
        if user_choice == 3:
            quit()
