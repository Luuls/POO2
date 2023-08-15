class Client:
    def __init__(self, name, telephone):
        self.__name = name
        self.__telephone = telephone


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, new_telephone):
        self.__telephone = new_telephone


class Account:
    def __init__(self, owners, balance=0):
        self.__owners = owners
        self.__balance = balance

    @property
    def owners(self):
        return self.__owners

    @owners.setter
    def owners(self, new_owners):
        self.__owners = new_owners

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def add_owner(self, owner):
        self.__owners.append(owner)

    def remove_owner_by_name(self, name):
        for i, owner in enumerate(self.__owners):
            if name == owner.name:
                self.__owners.pop(i)

    def deposit(self, value):
        if value < 0:
            raise ValueError

        self.__balance += value

    def withdraw(self, value):
        if value < 0:
            raise ValueError

        if value > self.balance:
            print(f'Saldo insuficiente. Tentando sacar R${value} de um total de R${self.balance}')

        self.__balance -= value


class Bank:
    def __init__(self, name, accounts=[]):
        self.__name = name
        self.__accounts = accounts

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, new_accounts):
        self.__accounts = new_accounts

    def _search(self, name):
        for i, account in enumerate(self.__accounts):
            for owner in account.owners:
                if name == owner.name:
                    return i
        
        return None

    def search_account_by_name(self, name):
        return self._search(name)

    def add_account(self, account):
        self.__accounts.append(account)

    def remove_account_by_name(self, name):
        return self._search(name)

    def __add__(self, other)
