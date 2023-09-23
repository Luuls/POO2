from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados: list[Chamado] = []
        self.__tipoChamados: list[TipoChamado] = []

    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        if not isinstance(tipo, TipoChamado):
            return -1

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
            return chamado

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
            return tipoChamado
        
        self.__tipoChamados.append(tipoChamado)
        return tipoChamado

    def tipoChamados(self) -> list[TipoChamado]:
        return self.__tipoChamados
