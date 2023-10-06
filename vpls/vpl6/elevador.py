from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, andarAtual: int, totalAndaresPredio: int,
                 capacidade: int, totalPessoas: int):
        self.__andarAtual = andarAtual
        self.__totalAndaresPredio = totalAndaresPredio
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas

    def descer(self) -> str:
        if self.andarAtual == 0:
            raise ElevadorJahNoTerreoException

        self.__andarAtual -= 1
        return f'Elevador foi para o andar {self.andarAtual}'

    def subir(self) -> str:
        if self.andarAtual == self.totalAndaresPredio - 1:
            raise ElevadorJahNoUltimoAndarException

        self.__andarAtual += 1
        return f'O elevador foi para o andar {self.andarAtual}'

    def entraPessoa(self) -> str:
        if self.totalPessoas == self.capacidade:
            raise ElevadorCheioException

        self.__totalPessoas += 1
        return f'O elevador esta comportando {self.totalPessoas} pessoas'

    def saiPessoa(self) -> str:
        if self.totalPessoas == 0:
            raise ElevadorJahVazioException

        self.__totalPessoas -= 1
        return f'O elevador esta comportando {self.totalPessoas} pessoas'

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @property
    def totalPessoas(self) -> int:
        return self.__totalPessoas

    @property
    def totalAndaresPredio(self) -> int:
        return self.__totalAndaresPredio

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int) -> None:
        self.__totalAndaresPredio = totalAndaresPredio

    @property
    def andarAtual(self) -> int:
        return self.__andarAtual

