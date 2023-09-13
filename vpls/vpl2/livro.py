from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int,
                 editora: Editora, autor: Autor,
                 numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]

    def incluirAutor(self, autor: Autor):
        if not isinstance(autor, Autor):
            return

        try:
            self.__procurar(self.autores, autor.codigo,
                            lambda x: x.codigo)

        # ValueError caso o autor não esteja na lista
        except ValueError:
            self.autores.append(autor)

    def excluirAutor(self, autor: Autor):
        if not isinstance(autor, Autor):
            return

        try:
            indice = self.__procurar(self.autores, autor.codigo,
                                     lambda x: x.codigo)

        except ValueError:
            return

        self.autores.pop(indice)

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        if not isinstance(numeroCapitulo, int) or \
                not isinstance(tituloCapitulo, str):
            return

        try:
            self.__procurar(self.capitulos, tituloCapitulo, lambda x: x.titulo)

        except ValueError:
            self.capitulos.append(Capitulo(numeroCapitulo, tituloCapitulo))

    def excluirCapitulo(self, tituloCapitulo: str):
        if not isinstance(tituloCapitulo, str):
            return

        try:
            indice = self.__procurar(self.capitulos, tituloCapitulo,
                                     lambda x: x.titulo)

        except ValueError:
            return

        self.capitulos.pop(indice)

    def findCapituloByTitulo(self, tituloCapitulo: str):
        if not isinstance(tituloCapitulo, str):
            return

        try:
            indice = self.__procurar(self.capitulos, tituloCapitulo,
                                     lambda x: x.titulo)

        except ValueError:
            return

        return self.capitulos[indice]

    def __procurar(self, conteiner, valor, chave=lambda x: x):
        for i, valorInterno in enumerate(conteiner):
            if valor == chave(valorInterno):
                return i

        raise ValueError('Valor não encontrado no contêiner')

    # getters e setters
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novoTitulo):
        self.__titulo = novoTitulo

    @property
    def capitulos(self):
        return self.__capitulos

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novoAno):
        self.__ano = novoAno

    @property
    def editora(self):
        return self.__editora

    @property
    def autores(self):
        return self.__autores
