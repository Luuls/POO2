class Transporte:
    def __init__(
            self,
            nome: str,
            altura: float,
            comprimento: float,
            carga: float,
            velocidade: float
        ):
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novoNome: str) -> None:
        self.__nome = novoNome


    @property
    def altura(self) -> float:
        return self.__altura

    @altura.setter
    def altura(self, novaAltura: float) -> None:
        self.__altura = novaAltura

    @property
    def comprimento(self) -> float:
        return self.__comprimento

    @comprimento.setter
    def comprimento(self, novoComprimento: float) -> None:
        if novoComprimento <= 0:
            raise ValueError

        self.__comprimento = novoComprimento
