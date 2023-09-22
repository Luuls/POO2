from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, tamanhoPasso):
        self.__tamanho_passo = tamanhoPasso


    def mover(self):
        return f'ANIMAL: DESLOCOU {self.__tamanho_passo}'

    @abstractmethod
    def produzir_som(self):
        pass

    @property
    def tamanho_passo(self):
        return self.__tamanho_passo

    @tamanho_passo.setter
    def tamanho_passo(self, novo_tamanho_passo):
        self.__tamanho_passo = novo_tamanho_passo
