from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self.name = name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self.age = age

class Account(ABC):

    def __init__(self, agency, account_number, balance):
        self._agency = agency
        self._account_number = account_number
        self._balance = balance

    @property
    def agency(self):
        return self._agency
    
    @agency.setter
    def agency(self, agency):
        self._agency = agency

    @property
    def account_number(self, account_number):
        return self._account_number
    
    @account_number.setter
    def account_number(self, account_number):
        self._account_number = account_number

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        self._balance = balance
    
    def deposit(self, value):
        self.balance += value

    @abstractmethod
    def withdraw(self, value):
        ...

class AccountChecking(Account):

    def __init__(self, agency, account_number, balance):
        super().__init__(agency, account_number, balance)

    def withdraw(self, value):
        if value > 1200:
            print("Value bigger than limit.")
            return self.balance
        
        else:
            if value > self.balance:
                print("Value bigger than balance.")
                return self.balance
            else:
                self.balance -= value
                return self.balance
            
class AccountSavings(Account):

    def __init__(self, agency, account_number, balance):
        super().__init__(agency, account_number, balance)

    def withdraw(self, value):
        if value > 800:
            print("Value bigger than limit.")
            return self.balance
        
        else:
            if value > self.balance:
                print("Value bigger than balance.")
                return self.balance
            else:
                self.balance -= value
                return self.balance
        
class Client(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self._account = None
    
    @property
    def account(self):
        return self._account
    
    @account.setter
    def account(self, account):
        self.account = account

class Bank:

    def __init__(self, *agencies):
        self.__agencies = [ag for ag in agencies]
        self.__accounts = []
        self.__clients = []

    @property
    def agencies(self):
        return self.__agencies

    @property
    def accounts(self):
        return self.__accounts
    
    @property
    def clients(self):
        return self.__clients

    def add_client_and_account(self, client, account):
        self.clients.append(client)
        self.accounts.append(account)

    def verify(self, agency, client, account):
        is_it = False

        if agency in self.agencies and client in self.clients and account in self.accounts:
            is_it = True

        return is_it
    
# Instances
b1 = Bank("1111", "2222", "3333")

c1 = Client("Joseph", 40)
c2 = Client("Leon", 35)

acc1 = AccountSavings(b1.agencies[0], "0111-X", 100)
acc2 = AccountChecking(b1.agencies[2], "0222-X", 3000)

b1.add_client_and_account(c1, acc1)
b1.add_client_and_account(c2, acc2)

b2 = Bank("5555", "6666", "7777")

c3 = Client("Ferdinand", 22)
c4 = Client("Swawn", 27)

acc3 = AccountSavings(b2.agencies[0], "0333-X", 20)
acc4 = AccountChecking(b2.agencies[2], "0444-X", 10000)

b2.add_client_and_account(c3, acc3)
b2.add_client_and_account(c4, acc4)

# Tests
print(b1.verify(b2.agencies[0], c4, acc3))
print(b1.verify(b1.agencies[0], c1, acc1))

print(acc1.withdraw(50))
print(acc1.withdraw(100))
print(b1.accounts[0].balance)

print(b2.accounts[1].withdraw(1000))
print(acc4.balance)