from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluirLivro(self, livro: Livro):
        if not isinstance(livro, Livro):
            raise TypeError

        try:
            self.__procurar(self.livros, livro.codigo, chave=lambda x: x.codigo)

        except ValueError:
            self.livros.append(livro)
            return

        raise ValueError(f'O livro {livro.codigo} já está cadastrado nesta biblioteca')

    def excluirLivro(self, livro: Livro):
        if not isinstance(livro, Livro):
            raise TypeError

        try:
            indice = self.__procurar(self.livros, livro.codigo, chave=lambda x: x.codigo)

        except ValueError:
            raise ValueError(f'O livro {livro.codigo} não está cadastrado nesta biblioteca')

        self.livros.pop(indice)
        return

    # não vou criar uma função global para todas as classes usarem, pois creio que no VPL não vá funcionar
    def __procurar(self, conteiner, valor, chave=lambda x: x):
        for i, valorInterno in enumerate(conteiner):
            if valor == chave(valorInterno):
                return i

        raise ValueError('Valor não encontrado no contêiner')

    @property
    def livros(self):
        return self.__livros
