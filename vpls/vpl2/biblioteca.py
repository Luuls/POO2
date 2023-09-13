from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluirLivro(self, livro: Livro):
        if not isinstance(livro, Livro):
            return

        try:
            self.__procurar(self.livros, livro.codigo,
                            lambda x: x.codigo)

        except ValueError:
            self.livros.append(livro)

    def excluirLivro(self, livro: Livro):
        if not isinstance(livro, Livro):
            return

        try:
            indice = self.__procurar(self.livros, livro.codigo,
                                     lambda x: x.codigo)

        except ValueError:
            return

        self.livros.pop(indice)

    # não vou criar uma função global
    # para todas as classes usarem,
    # pois creio que no VPL não vá funcionar
    def __procurar(self, conteiner, valor, chave=lambda x: x):
        for i, valorInterno in enumerate(conteiner):
            if valor == chave(valorInterno):
                return i

        raise ValueError('Valor não encontrado no contêiner')

    @property
    def livros(self):
        return self.__livros

