from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipoChamados = []

    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        if not isinstance(tipo, TipoChamado):
            return 0

        totalChamados = 0
        for chamado in self.__chamados:
            if chamado.tipo == tipo:
                totalChamados += 1

        return totalChamados

    def incluiChamado(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado) -> Chamado:
        if (
                not isinstance(data, Date) or
                not isinstance(cliente, Cliente) or
                not isinstance(tecnico, Tecnico) or
                not isinstance(titulo, str) or
                not isinstance(descricao, str) or
                not isinstance(prioridade, int) or
                not isinstance(tipo, TipoChamado)):
            return

        chamado = Chamado(
            data,
            cliente,
            tecnico,
            titulo,
            descricao,
            prioridade,
            tipo
        )

        try:
            self.pesquisar(self.__chamados, chamado)
        except ValueError:
            self.__chamados.append(chamado)

        return chamado

    def incluiTipoChamado(
            self,
            codigo: int,
            nome: str,
            descricao: str) -> TipoChamado:
        if (
                not isinstance(codigo, int) or
                not isinstance(nome, str) or
                not isinstance(descricao, str)):
            return

        tipoChamado = TipoChamado(codigo, descricao, nome)

        try:
            self.pesquisar(self.__tipoChamados, tipoChamado)
        except ValueError:
            self.__tipoChamados.append(tipoChamado)

        return tipoChamado

    @property
    def tipoChamados(self) -> list:
        return self.__tipoChamados

    def pesquisar(self, conteiner, valor, predicado=lambda x: x):
        for i, valorConteiner in enumerate(conteiner):
            if valor == predicado(valorConteiner):
                return i

        raise ValueError
