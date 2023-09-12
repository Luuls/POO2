from categoria_produto import CategoriaProduto
from cliente import Cliente


class Produto:
    def __init__(self, codigo: int,
                 descricao: str,
                 categoria: CategoriaProduto):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria = categoria

        self.__quantidade = 0
        self.__preco_unitario = 0
        self.__cliente = None

    def preco_total(self):
        return self.preco_unitario * self.quantidade

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        self.__descricao = nova_descricao

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, nova_categoria):
        self.__categoria = nova_categoria

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, novo_preco):
        self.__preco_unitario = novo_preco

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, novo_cliente):
        self.__cliente = novo_cliente
