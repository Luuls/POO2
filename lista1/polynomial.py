class Monomial:
    def __init__(self, degree: int, coefficient: float = 1):
        self.__degree = degree
        self.__coefficient = coefficient

    def __call__(self, input_value: float) -> float:
        return self.__coefficient * input_value ** self.__degree

    def multiply_by_constant(self, value: float) -> 'Monomial':
        return Monomial(self.__degree, self.__coefficient * value)

    def multiply_by_constant_in_place(self, value: float) -> 'Monomial':
        self.__coefficient *= value
        return self

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
        if self.__degree == 0:
            return f'{self.__coefficient}'

        return f'{self.__coefficient}x^{self.__degree}'

    def __repr__(self) -> str:
        return str(self)


class Polynomial:
    def __init__(self, terms: list[Monomial]):
        if len(terms) == 0:
            raise BufferError('Cannot construct a polynomial with 0 terms')
            
        self.__terms = sorted(terms, key=lambda term: term.get_degree(), reverse=True)
        self.__degree = self.__terms[-1].get_degree()

    def __call__(self, input_value: float) -> float:
        result: float = 0
        for term in self.__terms:
            result += term.__call__(input_value)

        return result
        
    def multiply_by_constant(self, value: float) -> 'Polynomial':
        '''returns a new polynomial with terms multiplied by the constant passed to the method'''
        new_terms: list[Monomial] = []
        for term in self.__terms:
            new_terms.append(term.multiply_by_constant(value))

        return Polynomial(new_terms)

    def multiply_by_constant_in_place(self, value) -> 'Polynomial':
        for i, term in enumerate(self.__terms):
            self.__terms[i].multiply_by_constant_in_place(value)

        return self

    def get_terms(self) -> list[Monomial]:
        return self.__terms.copy()

    def set_terms(self, new_terms: list[Monomial]) -> None:
        self.__terms = new_terms
        self.__degree = self.__terms[-1].get_degree()

    def get_degree(self) -> int:
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

                self_index += self_index < self_len
                other_index += other_index < other_len

            elif self_term.get_degree() > other_term.get_degree():
                result.append(other_term)
                other_index += other_index < other_len

            elif self_term.get_degree() < other_term.get_degree():
                result.append(self_term)
                self_index += self_index < self_len

        return Polynomial(result)

    def __sub__(self, other) -> 'Polynomial':
        return self.multiply_by_constant(-1) + other
        
    def __str__(self) -> str:
        return ' + '.join([str(term) for term in self.__terms])

    def __repr__(self) -> str:
        return str(self)


pol1 = Polynomial([Monomial(2), Monomial(0), Monomial(1), Monomial(3), Monomial(5, -1)])
print(f'pol1:  {pol1}')

pol2 = Polynomial([Monomial(3), Monomial(4), Monomial(5)])
print(f'pol2:  {pol2}')
print(f'pol1 + pol2 = {pol1 + pol2}')
print(f'pol1 - pol2 = {pol1 - pol2}')

print(f'{pol1(0) = }')
print(f'{pol1(1) = }')
print(f'{pol1(2) = }')
print(f'{pol1(5) = }')
print('\n')
print(f'{pol2(0) = }')
print(f'{pol2(1) = }')
print(f'{pol2(2) = }')
print(f'{pol2(5) = }')
