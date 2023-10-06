from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = Elevador(0, 0, 0, 0)

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def inicializarElevador(self, capacidade, totalPessoas,
                 totalAndaresPredio, andarAtual) -> None:

        argumentos = [
            capacidade,
            totalPessoas,
            totalAndaresPredio,
            andarAtual
        ]

        for argumento in argumentos:
            if not isinstance(argumento, int) or argumento < 0:
                raise ComandoInvalidoException

        if andarAtual > totalAndaresPredio or totalPessoas > capacidade:
            raise ComandoInvalidoException

        self.__elevador = Elevador(*argumentos)

    def subir(self) -> str:
        return self.elevador.subir()

