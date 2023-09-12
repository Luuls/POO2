from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor] 

    def incluirAutor(self, autor: Autor):

    def excluirAutor(self, autor: Autor):

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):

    def excluirCapitulo(self, tituloCapitulo: str):

    def findCapituloByTitulo(self, tituloCapitulo: str):

    def __procurar(self, conteiner, valor, chave=lambda valor: valor):

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
