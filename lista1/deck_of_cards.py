'''À princípio, essas classes foram designadas para implementar quaisquer jogos de carta'''

import random

class Card:
    def __init__(self, value: int | str = 0, title='', description=''):
        self.__value = value

        # Título e descrição para caso o jogo seja um RPG ou qualquer jogo em que as cartas possuam texto/imagem
        self.__title = title
        self.__description = description

    # Pode ser sobrescrita (herança) para gerar alguma ação (uma carta especial, por exemplo)
    def action(self) -> None:
        pass

    def get_value(self) -> int | str:
        return self.__value

    def set_value(self, new_value: int | str) -> None:
        self.__value = new_value

    def get_title(self) -> str:
        return self.__title

    def set_title(self, new_title: str):
        self.__title = new_title

    def get_description(self) -> str:
        return self.__description

    def set_description(self, new_description):
        self.__description = new_description


class Deck:
    def __init__(self, cards: list[Card]):
        self.__cards = cards

    def get_cards(self) -> list[Card]:
        return self.__cards

    def cards_amount(self) -> int:
        return len(self.__cards)

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

    def retrieve_card(self, index: int) -> Card:
        ''' Retorna a carta na posição >index<. Passe -1 no parâmetro index para escolher aleatoriamente'''
        if index == -1:
            index = random.randint(0, len(self.__cards) - 1)

        elif not (0 <= index < len(self.__cards)):
            raise IndexError('Index out of bounds')

        return self.__cards.pop(index)

    def retrieve_n_cards(self, *indexes: int) -> list[Card]:
        '''
        Se apenas um índice for passado, retorna uma lista de cartas aleatórias com o tamanho do índice.
        Se mais índices forem passados, retorna as respectivas cartas da lista
        '''

        cards: list[Card] = []
        if len(indexes) == 1:
            index = indexes[0]
            if index >= len(self.__cards):
                raise IndexError('The passed index is out of bounds')

            for i in range(index):
                cards.append(self.__cards.pop(random.randint(0, len(self.__cards) - 1 - i)))

            return cards

        for index in sorted(indexes, reverse=True):
            cards.append(self.__cards.pop(index))

        return cards

    def add_card(self, card: Card) -> None:
        self.__cards.append(card)

    def __getitem__(self, index: int) -> Card:
        return self.__cards[index]

