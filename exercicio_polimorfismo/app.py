from abc import ABC, abstractmethod


class Transporte(ABC):
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

    def __str__(self) -> str:
        resultado = f'Nome: {self.nome}\n'
        resultado += f'Altura: {self.altura} m\n'
        resultado += f'Comprimento: {self.comprimento} m\n'
        resultado += f'Carga: {self.carga} t\n'
        resultado += f'Velocidade: {self.velocidade} km/s\n'
        return resultado

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
        if novaAltura <= 0:
            raise ValueError

        self.__altura = novaAltura

    @property
    def comprimento(self) -> float:
        return self.__comprimento

    @comprimento.setter
    def comprimento(self, novoComprimento: float) -> None:
        if novoComprimento <= 0:
            raise ValueError

        self.__comprimento = novoComprimento

    @property
    def carga(self) -> float:
        return self.__carga

    @carga.setter
    def carga(self, novaCarga: float) -> None:
        if novaCarga <= 0:
            raise ValueError

        self.__carga = novaCarga

    @property
    def velocidade(self) -> float:
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, novaVelocidade: float) -> None:
        if novaVelocidade <= 0:
            raise ValueError

        self.__velocidade = novaVelocidade


class TransporteAereo(Transporte):
    def __init__(
            self,
            nome: str,
            altura: float,
            comprimento: float,
            carga: float,
            velocidade: float,
            autonomia: float,
            envergadura: float
        ):

        Transporte.__init__(
            self,
            nome,
            altura,
            comprimento,
            carga,
            velocidade
        )

        self.__autonomia = autonomia
        self.__envergadura = envergadura


    def __str__(self) -> str:
        resultado = Transporte.__str__(self)
        resultado += f'Autonomia: {self.autonomia} km\n'
        resultado += f'Envergadura: {self.envergadura} m\n'
        return resultado

    @property
    def autonomia(self) -> float:
        return self.__autonomia

    @autonomia.setter
    def autonomia(self, novaAutonomia: float) -> None:
        if novaAutonomia <= 0:
            raise ValueError

        self.__autonomia = novaAutonomia

    @property
    def envergadura(self) -> float:
        return self.__envergadura

    @envergadura.setter
    def envergadura(self, novaEnvergadura: float) -> None:
        if novaEnvergadura <= 0:
            raise ValueError

        self.__envergadura = novaEnvergadura


class TransporteTerrestre(Transporte):
    def __init__(
            self,
            nome: str,
            altura: float,
            comprimento: float,
            carga: float,
            velocidade: float,
            motor: str,
            rodas: str
        ):

        Transporte.__init__(
            self,
            nome,
            altura,
            comprimento,
            carga,
            velocidade
        )

        self.__motor = motor
        self.__rodas = rodas

    def __str__(self) -> str:
        resultado = Transporte.__str__(self)
        resultado += f'Motor: {self.motor}\n'
        resultado += f'Rodas: {self.rodas}\n'
        return resultado

    @property
    def motor(self) -> str:
        return self.__motor

    @motor.setter
    def motor(self, novoMotor: str) -> None:
        self.__motor = novoMotor

    @property
    def rodas(self) -> str:
        return self.__rodas

    @rodas.setter
    def rodas(self, novasRodas: str) -> None:
        self.__rodas = novasRodas


class TransporteAquatico(Transporte):
    def __init__(
            self,
            nome: str,
            altura: float,
            comprimento: float,
            carga: float,
            velocidade: float,
            boca: float,
            calado: float
        ):

        Transporte.__init__(
            self,
            nome,
            altura,
            comprimento,
            carga,
            velocidade
        )

        self.__boca = boca
        self.__calado = calado

    def __str__(self) -> str:
        resultado = Transporte.__str__(self)
        resultado += f'Boca: {self.boca} m\n'
        resultado += f'Calado: {self.calado} m\n'
        return resultado

    @property
    def boca(self) -> float:
        return self.__boca

    @boca.setter
    def boca(self, novaBoca: float) -> None:
        if novaBoca <= 0:
            raise ValueError

        self.__boca = novaBoca

    @property
    def calado(self) -> float:
        return self.__calado

    @calado.setter
    def calado(self, novoCalado: float) -> None:
        if novoCalado <= 0:
            raise ValueError

        self.__calado = novoCalado


class Catalogo:
    def __init__(self, veiculos: list[Transporte]):
        self.__veiculos = veiculos

    @property
    def veiculos(self) -> list[Transporte]:
        return self.__veiculos

    def incluirVeiculo(self, veiculo: Transporte):
        if not isinstance(veiculo, Transporte):
            raise TypeError

        self.veiculos.append(veiculo)

    def mostrarVeiculosTransporte(self) -> None:
        print('Bem vindo ao nosso catálogo! Abaixo estão os veículos aqui disponíveis.')
        for veiculo in self.veiculos:
            print('\n' + '-' * 10)
            print(veiculo)


veiculos = [
    TransporteTerrestre('uno', 2.20, 4.0, 10, 400, 'de fusca', 'quadrada'),
    TransporteAereo('jato azul', 3, 15, 40, 600, 1000, 42.3),
]

catalogo = Catalogo(veiculos)
catalogo.incluirVeiculo(TransporteAquatico('cruzeiro', 30, 62.5, 100, 60, 13.20, 1))

catalogo.mostrarVeiculosTransporte()

