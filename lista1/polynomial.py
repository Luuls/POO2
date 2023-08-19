class Monomial:
    def __init__(self, degree: int, coefficient: float = 1):
        self.__degree = degree
        self.__coefficient = coefficient

    def get_degree(self):
        return self.__degree

    def set_degree(self, value: int):
        self.__degree = value

    def get_coefficient(self):
        return self.__coefficient

    def set_coefficient(self, value: int):
        self.__coefficient = value


class Polynomial:
    def __init__(self, terms: list[Monomial]):
        self.__terms = terms
        
    def get_terms(self):
        return self.__terms.copy()

    def set_terms(self, new_terms: list[Monomial]):
        self.__terms = new_terms


pol1 = Polynomial([Monomial(0), Monomial(1), Monomial(2)])
