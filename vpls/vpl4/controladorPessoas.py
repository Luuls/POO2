from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        if not isinstance(codigo, int) or not isinstance(nome, str):
            return

        cliente = Cliente(nome, codigo)

        try:
            self.pesquisar(self.clientes, cliente)
        except ValueError:
            self.clientes.append(cliente)

        return cliente

    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        if not isinstance(codigo, int) or not isinstance(nome, str):
            return

        tecnico = Tecnico(nome, codigo)

        try:
            self.pesquisar(self.tecnicos, tecnico)
        except ValueError:
            self.tecnicos.append(tecnico)

        return tecnico

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def pesquisar(self, conteiner, valor, predicado=lambda x: x):
        for i, valorConteiner in enumerate(conteiner):
            if valor == predicado(valorConteiner):
                return i

        raise ValueError
