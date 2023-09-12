class Capitulo:
    def __init__(self, numero: int, titulo: str):
        self.__numero = numero
        self.__titulo = titulo

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, novoNumero):
        self.__numero = novoNumero

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novoTitulo):
        self.__titulo = novoTitulo
