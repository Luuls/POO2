from ave import Ave


class Canarinho(Ave):
    def __init__(self, tamanhoPasso, alturaVoo):
        Ave.__init__(self, tamanhoPasso, alturaVoo)

    def produzir_som(self):
        return Ave.produzir_som(self) + ' PIU'

    def cantar(self):
        return self.produzir_som()

