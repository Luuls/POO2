from mamifero import Mamifero


class Cachorro(Mamifero):
    def __init__(self):
        Mamifero.__init__(self, 3, 3)

    def produzir_som(self):
        result = Mamifero.produzir_som(self)
        result += 'AU'
        return result

    def latir(self):
        return self.produzir_som()

