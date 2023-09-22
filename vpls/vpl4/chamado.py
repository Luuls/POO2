from abstractChamado import AbstractChamado
from tipoChamado import TipoChamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class Chamado(AbstractChamado):
    def __init__(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado):
        self.__data = data
        self.__cliente = cliente
        self.__tecnico = tecnico
        self.__titulo = titulo
        self.__descricao = descricao
        self.__prioridade = prioridade
        self.__tipo = tipo

    def __eq__(self, other):
        if not isinstance(other, Chamado):
            return False

        return (
            self.data == other.data and
            self.cliente == other.cliente and
            self.tecnico == other.tecnico and
            self.tipo == other.tipo
        )

    @property
    def data(self) -> Date:
        return self.__data

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def tecnico(self) -> Tecnico:
        return self.__tecnico

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def prioridade(self) -> int:
        return self.__prioridade

    @property
    def tipo(self) -> TipoChamado:
        return self.__tipo
