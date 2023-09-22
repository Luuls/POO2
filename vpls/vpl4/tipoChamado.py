from abstractTipoChamado import AbstractTipoChamado


class TipoChamado(AbstractTipoChamado):
    def __init__(self, codigo: int, descricao: str, nome: str):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__nome = nome

    def __eq__(self, other):
        if not isinstance(other, TipoChamado):
            return False
        
        return self.codigo == other.codigo

    def codigo(self) -> int:
        return self.__codigo

    def descricao(self) -> str:
        return self.__descricao

    def nome(self) -> str:
        return self.__nome
