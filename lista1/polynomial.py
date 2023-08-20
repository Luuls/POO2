class Monomial:
    def __init__(self, degree: int, coefficient: float = 1):
        self.__degree = degree
        self.__coefficient = coefficient

    def compute(self, input_value: int) -> float:
        return self.__coefficient * input_value ** self.__degree

    def multiply_by_constant(self, value: float):
        self.__coefficient *= value

    def get_degree(self) -> int:
        return self.__degree

    def set_degree(self, value: int):
        self.__degree = value

    def get_coefficient(self) -> float:
        return self.__coefficient

    def set_coefficient(self, value: int):
        self.__coefficient = value

    def __add__(self, other: 'Monomial') -> 'Monomial':
        return Monomial(self.__degree, self.__coefficient + other.get_coefficient())

    def __str__(self) -> str:
        return f'{self.__coefficient}x^{self.__degree}'

    def __repr__(self) -> str:
        return str(self)


class Polynomial:
    def __init__(self, terms: list[Monomial]):
        if len(terms) == 0:
            raise BufferError('Cannot construct a polynomial with 0 terms')
            
        self.__terms = sorted(terms, key=lambda term: term.get_degree())
        self.__degree = self.__terms[-1].get_degree()

    def compute(self, input_value) -> float:
        result: float = 0
        for term in self.__terms:
            result += term.compute(input_value)

        return result
        
    def multiply_by_constant(self, value) -> 'Polynomial':
        '''returns a new polynomial with terms multiplied by the passed constant'''
        new_terms = self.__terms.copy()
        for i, term in enumerate(self.__terms):
            new_terms[i].multiply_by_constant(value)

        return Polynomial(new_terms)

    def multiply_by_constant_in_place(self, value):
        for i, term in enumerate(self.__terms):
            self.__terms[i].multiply_by_constant(value)

    def get_terms(self) -> list[Monomial]:
        return self.__terms.copy()

    def set_terms(self, new_terms: list[Monomial]) -> None:
        self.__terms = new_terms
        self.__degree = self.__terms[-1].get_degree()

    def get_degree(self):
        return self.__degree

    def __add__(self, other: 'Polynomial') -> 'Polynomial':
        self_index = other_index = 0
        self_len = len(self.__terms)

        other_terms = other.get_terms()
        other_len = len(other_terms)

        result: list[Monomial] = []
        while self_index < self_len or other_index < other_len:
            self_term = self.__terms[self_index]
            other_term = other_terms[other_index]

            if self_term.get_degree() == other_term.get_degree():
                terms_sum = self_term + other_term
                if terms_sum.get_coefficient() != 0:
                    result.append(terms_sum)

                if self_index < self_len:
                    self_index += 1

                if other_index < other_len:
                    other_index += 1

            elif self_term.get_degree() > other_term.get_degree():
                result.append(other_term)
                if other_index < other_len:
                    other_index += 1

            elif self_term.get_degree() < other_term.get_degree():
                result.append(self_term)
                if self_index < self_len:
                    self_index += 1

        return Polynomial(result)

    def __sub__(self, other):
        return self.multiply_by_constant(-1) + other
        
    def __repr__(self) -> str:
        return ' + '.join([str(term) for term in self.__terms])


pol1 = Polynomial([Monomial(2), Monomial(0), Monomial(1), Monomial(3), Monomial(5)])
print(f'  {pol1}')

pol2 = Polynomial([Monomial(3), Monomial(4), Monomial(5)])
print(f'+ {pol2}')
print(f'\n= {pol1 + pol2}')

print(pol1.compute(0))
print(pol1.compute(1))
print(pol1.compute(2))

print(pol2.compute(5))
