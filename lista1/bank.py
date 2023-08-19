import datetime
from abc import ABC

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

    def __repr__(self) -> str:
        return f'<{self.__name}, {self.__telephone}>'
        

class Operation(ABC):
    def __init__(self, date, value):
        self.__date = date
        self.__value = value

    @property
    def date(self):
        return self.__date

    @property
    def value(self):
        return self.__value


class Withdraw(Operation):
    __operation = 'Saque'

    def __init__(self, date, value):
        Operation.__init__(self, date, value)

    @property
    def operation(self):
        return Withdraw.__operation


class Deposit(Operation):
    __operation = 'Depósito'

    def __init__(self, date, value):
        Operation.__init__(self, date, value)

    @property
    def operation(self):
        return Deposit.__operation


class Yield(Operation):
    __operation = 'Rendimento'

    def __init__(self, date, value):
        Operation.__init__(self, date, value)

    @property
    def operation(self):
        return Yield.__operation

class Account(ABC):
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

        self.balance += value
        self._create_operation(Deposit, value)

    def withdraw(self, value):
        if value < 0:
            raise ValueError

        if value > self.balance:
            print(f'Saldo insuficiente. Tentando sacar R${value} de um total de R${self.balance}')

        self.balance -= value
        self._create_operation(Withdraw, value)

    def _create_operation(self, operation_constructor: type[Operation], value):
        current_datetime = datetime.datetime.now()
        current_operation = operation_constructor(current_datetime, value)
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


class CheckingAccount(Account):
    def __init__(self, owners, balance=0):
        Account.__init__(self, owners, balance)


class AdditionalLimitAccount(Account):
    def __init__(self, owners, balance=0, additional_limit=0):
        Account.__init__(self, owners, balance)
        self.__additional_limit = additional_limit

    def withdraw(self, value):
        if value < 0:
            raise ValueError

        total_balance = self.balance + self.__additional_limit
        if value > total_balance:
            print(f'Saldo insuficiente. Tentando sacar R${value} de um total de R${self.balance} + R${self.__additional_limit} = R${total_balance}')

        self.balance -= value
        self._create_operation(Withdraw, value)

    def add_limit(self, limit):
        '''aceita valores negativos'''
        self.__additional_limit += limit

    @property
    def additional_limit(self):
        return self.__additional_limit

    @additional_limit.setter
    def additional_limit(self, new_limit):
        self.__additional_limit = new_limit


class SavingsAccount(Account):
    def __init__(self, owners, balance=0):
        Account.__init__(self, owners, balance)
        self.__rate_of_interest = 0.05

    def update(self):
        pass

    def last_operation_date(self):
        if len(self.operations) == 0:
            raise BufferError

        return self.operations[-1].date

    def increase_balance(self):
        value = self.balance * self.__rate_of_interest
        self.balance += value
        self._create_operation(Yield, value)


class Bank:
    def __init__(self, name, accounts=[]):
        self.__name = name
        self.__accounts = accounts

        # lista de contas poupança só pra facilitar o percorrimento
        self.__saving_accounts = []

    def get_account_by_name(self, name):
        return self.__accounts[self.__search(name)]

    def add_checking_account(self, owners, balance=0):
        self.__accounts.append(CheckingAccount(owners, balance))

    def add_additional_limit_account(self, owners, balance=0, additional_limit=0):
        self.__accounts.append(AdditionalLimitAccount(owners, balance, additional_limit))

    def add_savings_account(self, owners, balance=0):
        account = SavingsAccount(owners, balance)
        self.__saving_accounts.append(account)
        self.__accounts.append(account)

    def remove_account_by_name(self, name):
        account_index = self.__search(name)
        self.__accounts.pop(account_index)

    def update(self):
        for i, account in enumerate(self.__saving_accounts):
            current_date = datetime.datetime.now()
            time_difference = current_date - account.last_operation_date()

            # rendendo a cada 3 segundos para efeito de teste. O certo seria a cada 1 mês
            if time_difference.total_seconds() >= 3:
                savings_account = self.__saving_accounts[i]
                savings_account.increase_balance()
                print(f'Conta de {savings_account.owners} rendendo. Saldo: {savings_account.balance}')

    def __search(self, name):
        for i, account in enumerate(self.__accounts):
            for owner in account.owners:
                if name == owner.name:
                    return i
        
        return None

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


clients = [Client('Luan', '48984449999')]
bank = Bank('Tatu')

bank.add_checking_account(clients, 400)
bank.add_savings_account([Client('Jonata', '4820232023')], 10**6)

acc = bank.get_account_by_name('Luan')
acc.deposit(502)
acc.withdraw(2)
acc.deposit(3)
acc.withdraw(200)
acc.withdraw(200)

print(f'Titulares da conta: {acc.owners}')
for operation in acc.operations:
    formatted_time = operation.date.strftime('%d/%m/%Y %H:%M:%S')
    print(f'{operation.operation}: R${operation.value:.2f}, {formatted_time}')

savings = bank.get_account_by_name('Jonata')
savings.deposit(800)

comparing_time = datetime.datetime.now()
while True:
    bank.update()
