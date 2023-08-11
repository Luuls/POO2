class Client:
    def __init__(self, name, telephone):
        self.name = name
        self.telephone = telephone


class Account:
    def __init__(self, owners, balance=0):
        self.owners = owners
        self.balance = balance

    def add_owner(self, owner):
        self.owners.append(owner)

    def remove_owner_by_name(self, name):
        for i, owner in enumerate(self.owners):
            if name == owner.name:
                self.owners.pop(i)

    def deposit(self, value):
        if value < 0:
            raise ValueError

        self.balance += value

    def withdraw(self, value):
        if value < 0:
            raise ValueError

        if value > self.balance:
            print(f'Saldo insuficiente. Tentando sacar R${value} de um total de R${self.balance}')

        self.balance -= value


class Bank:
    def __init__(self, name, accounts=[]):
        self.name = name
        self.accounts = accounts

    def _search(self, name):
        for i, account in enumerate(self.accounts):
            for owner in account.owners:
                if name == owner.name:
                    return i
        
        return None

    def search_account_by_name(self, name):
        return self._search(name)

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account_by_name(self, name):
        return self._search(name)

