from mamifero import Mamifero


class Gato(Mamifero):
    def __init__(self):
        Mamifero.__init__(self, 2, 2)

    def produzir_som(self):
        result = Mamifero.produzir_som(self)
        result += 'MIAU'
        return result

    def miar(self):
        return self.produzir_som()

