from abc import abstractmethod

from animal import Animal


class Ave(Animal):
    def __init__(self, tamanhoPasso, alturaVoo):
        Animal.__init__(self, tamanhoPasso)
        self.__altura_voo = alturaVoo

    def mover(self):
        return Animal.mover(self) + ' VOANDO'

    @abstractmethod
    def produzir_som(self):
        return 'AVE: PRODUZ SOM:'

    @property
    def altura_voo(self):
        return self.__altura_voo

    @altura_voo.setter
    def altura_voo(self, nova_altura_voo):
        self.__altura_voo = nova_altura_voo

