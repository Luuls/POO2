from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = Elevador(0, 0, 0, 0)

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int,
                            capacidade: int, totalPessoas: int) -> None:

        argumentos = [
            andarAtual,
            totalAndaresPredio,
            capacidade,
            totalPessoas
        ]

        for argumento in argumentos:
            if not isinstance(argumento, int) or argumento < 0:
                raise ComandoInvalidoException

        if andarAtual >= totalAndaresPredio or totalPessoas > capacidade:
            raise ComandoInvalidoException

        self.__elevador = Elevador(
            andarAtual,
            totalAndaresPredio,
            capacidade,
            totalPessoas
        )

    def subir(self) -> str:
        return self.elevador.subir()

    def descer(self) -> str:
        return self.elevador.descer()

    def entraPessoa(self) -> str:
        return self.elevador.entraPessoa()

    def saiPessoa(self) -> str:
        return self.elevador.saiPessoa()

