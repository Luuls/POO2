from abc import abstractmethod

from animal import Animal


class Mamifero(Animal):
    def __init__(self, volumeSom, tamanhoPasso):
        Animal.__init__(self, tamanhoPasso)
        self.__volume_som = volumeSom

    @abstractmethod
    def produzir_som(self):
        return f'MAMIFERO: PRODUZ SOM: {self.volume_som} SOM: '

    @property
    def volume_som(self):
        return self.__volume_som

    @volume_som.setter
    def volume_som(self, novo_volume):
        self.__volume_som = novo_volume
