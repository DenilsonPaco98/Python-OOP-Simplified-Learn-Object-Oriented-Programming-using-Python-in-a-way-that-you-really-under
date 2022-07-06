from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposite():
        return 0
    @abstractmethod
    def displayBalance():
        return 0

class SavingAccount(Account):
    def __init__(self) -> None:
        self.savingAccounts = {}
    def createAccount(self, name, initialDeposite):
        self.accountNumber = randint(10000, 99999)
        self.savingAccounts[self.accountNumber] = [name, initialDeposite]
        print("Account creation has been sucessful. You account number is: ", self.accountNumber)

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name:
                print("Authentication Sucessful!")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authenticate Failed.")
                return False
        else:
            print("Authenticate Failed.")
            return False
    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.savingAccounts[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingAccounts[self.accountNumber][1] -= withdrawAmount
            print("Withdrawal was sucessful.")
            self.displayBalance()

    def deposite(self, depositeAmount):
        self.savingAccounts[self.accountNumber][1] += depositeAmount
        print("Deposite was sucessful.")
        self.displayBalance()

    def displayBalance(self):
        print("Available balance: ", self.savingAccounts[self.accountNumber][1])

savingAccount = SavingAccount()
while True:
    print("Welcome banking online !!!")
    print("======================================")
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    print("======================================")
    userChoice = int(input("Enter you option: "))
    print()
    if userChoice is 1:
        print()
        print("Enter your name: ")
        name = input()
        print("Enter the initial deposit: ")
        deposit = int(input())
        savingAccount.createAccount(name, deposit)
        print()
    elif userChoice is 2:
        print()
        print("Enter your name: ")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        authenticationStatus = savingAccount.authenticate(name, accountNumber)
        print()
        if authenticationStatus is True:
            while True:
                print()
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display avialable balance")
                print("Enter 4 to go back to the previous menu")
                userChoice = int(input())
                print()
                if userChoice is 1:
                    print()
                    print("Enter a withdrawal amount")
                    withdrawalAmount = int(input())
                    savingAccount.withdraw(withdrawalAmount)
                    print()
                elif userChoice is 2:
                    print()
                    print("Enter an amount to be deposited")
                    depositeAmount = int(input())
                    savingAccount.deposite(depositeAmount)
                    print()
                elif userChoice is 3:
                    print()
                    savingAccount.displayBalance()
                    print()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
        print("Thanks for utilise banking online !")
        quit()
