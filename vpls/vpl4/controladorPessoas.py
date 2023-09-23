from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes: list[Cliente] = []
        self.__tecnicos: list[Tecnico] = []

    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        if not isinstance(codigo, int) or not isinstance(nome, str):
            return

        cliente = Cliente(nome, codigo)

        try:
            self.pesquisar(self.clientes, cliente)
        except ValueError:
            return cliente

        self.clientes.append(cliente)

    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        if not isinstance(codigo, int) or not isinstance(nome, str):
            return

        tecnico = Tecnico(nome, codigo)

        try:
            self.pesquisar(self.clientes, tecnico)
        except ValueError:
            return tecnico

        self.clientes.append(tecnico)


    def clientes(self) -> list[Cliente]:
        return self.__clientes

    def tecnicos(self) -> list[Tecnico]:
        return self.__tecnicos

