from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa


class Pessoa(AbstractPessoa, ABC):
    def __init__(self, nome: str, codigo: int):
        self.__nome = nome
        self.__codigo = codigo

    def __eq__(self, other) -> bool:
        if not isinstance(other, Pessoa):
            return False

        return self.codigo == other.codigo

    def nome(self) -> str:
        return self.__nome

    def codigo(self) -> int:
        return self.__codigo
