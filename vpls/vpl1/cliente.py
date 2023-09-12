class Cliente:
    def __init__(self, nome, fone):
        self.__nome = nome
        self.__fone = fone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, novo_fone):
        self.__fone = novo_fone
