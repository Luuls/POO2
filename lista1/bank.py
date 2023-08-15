import datetime

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

class Operation:
    def __init__(self, date, operation, value):
        self.__date = date
        self.__operation = operation
        self.__value = value

    @property
    def date(self):
        return self.__date

    @property
    def operation(self):
        return self.__operation

    @property
    def value(self):
        return self.__value

class CheckingAccount:
    def __init__(self, owners, balance=0):
        self.__owners = owners
        self.__balance = balance
        self.__operations = []

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
        self.__create_operation('Depósito', value)

    def withdraw(self, value):
        if value < 0:
            raise ValueError

        if value > self.balance:
            print(f'Saldo insuficiente. Tentando sacar R${value} de um total de R${self.balance}')

        self.__balance -= value
        self.__create_operation('Saque', value)

    def __create_operation(self, operation, value):
        current_datetime = datetime.datetime.now()
        current_operation = Operation(current_datetime, operation, value)
        self.__operations.append(current_operation)

    @property
    def owners(self):
        return self.__owners

    @owners.setter
    def owners(self, new_owners):
        if len(new_owners) == 0:
            raise BufferError

        self.__owners = new_owners

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    @property
    def operations(self):
        return self.__operations.copy()


class AdditionalLimitAccount(CheckingAccount):
    def __init__(self, owners, balance=0, additional_limit=0):
        super().__init__(owners, balance)
        self.__additional_limit = additional_limit

    @property
    def additional_limit(self):
        return self.__additional_limit

    @additional_limit.setter
    def additional_limit(self, new_limit):
        self.__additional_limit = new_limit

    def add_limit(self, limit):
        '''aceita valores negativos'''
        self.__additional_limit += limit


class SavingsAccount(CheckingAccount):
    def __init__(self, owners, balance=0):
        super().__init__(owners, balance)
        self.__rate_of_interest = 0.05

    def increase_balance(self):
        self.__balance *= (1 + self.__rate_of_interest)


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


clients = [Client('Luan', '48984449999')]
acc = CheckingAccount(clients, 400)
acc.deposit(502)
acc.withdraw(2)
acc.deposit(3)
acc.withdraw(200)
acc.withdraw(200)

for operation in acc.operations:
    formatted_time = operation.date.strftime('%d/%m/%Y %H:%M:%S')
    print(f'{operation.operation}: R${operation.value:.2f}, {formatted_time}')


