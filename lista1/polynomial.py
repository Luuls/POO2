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

    def __mul__(self, other: 'Monomial') -> 'Monomial':
        return Monomial(self.__degree + other.get_degree(), self.__coefficient * other.get_coefficient())

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
        self.__degree = self.__terms[0].get_degree()

    def __call__(self, input_value: float) -> float:
        result: float = 0
        for term in self.__terms:
            result += term.__call__(input_value)

        return result

    def plot(self):
        pass
        
    def multiply_by_constant(self, value: float) -> 'Polynomial':
        '''Retorna um novo polinômio com os termos multiplicados pela constante que foi passada para o método'''
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
        self.__terms = sorted(terms, key=lambda term: term.get_degree(), reverse=True) 

        self.__degree = self.__terms[0].get_degree()

    def get_degree(self) -> int:
        return self.__degree

    def __add__(self, other: 'Polynomial') -> 'Polynomial':
        # mapeia de grau para coeficiente
        result: dict[int, float] = {}

        for monomial in (self.__terms + other.get_terms()):
            result[monomial.get_degree()] = result.get(monomial.get_degree(), 0) + monomial.get_coefficient()

        no_zeros_result = [Monomial(degree, coefficient) for degree, coefficient in result.items() if coefficient != 0]
        return Polynomial(no_zeros_result)

    def __sub__(self, other: 'Polynomial') -> 'Polynomial':
        return self.multiply_by_constant(-1) + other

    def __mul__(self, other: 'Polynomial') -> 'Polynomial':
        partial_pols: list[list[Monomial]] = [[] for _ in range(len(self.__terms))]
        for i, self_term in enumerate(self.__terms):
            for other_term in other.get_terms():
                partial_pols[i].append(self_term * other_term)

        result = Polynomial([Monomial(0, 0)])
        for pol in partial_pols:
            result += Polynomial(pol)

        return result
        
    def __str__(self) -> str:
        return ' + '.join([str(term) for term in self.__terms])

    def __repr__(self) -> str:
        return str(self)


if __name__ == '__main__':
    print('Calculadora de polinômios')

    polynomials: dict[str, Polynomial] = {}
    names = ['p', 'q']
    for name in names:
        print(f'\nPreenchimento do polinômio {name}(x)')
        print('Pressione EOF -> CTRL + Z (Windows) ou CTRL + D (Linux) para finalizar\n')
        i = 0
        terms: list[Monomial] = []
        while True:
            try:
                coefficient = float(input(f'Insira o coeficiente do {i + 1}° termo (grau {i}): '))

            except EOFError:
                print('\n')
                break

            if coefficient != 0:
                terms.append(Monomial(i, coefficient))

            i += 1

        polynomials[name] = Polynomial(terms)

    p, q = polynomials.values()
    options = ['somar', 'multiplicar', 'acessar o grau', 'calcular']
    while True:
        print(f'p(x) = {p}')
        print(f'q(x) = {q}')

        print('Selecione uma opção (EOF para sair):')
        for i, option in enumerate(options):
            print(f'[{i + 1}] {option}')

        try:
            option_chosen = int(input('\n'))

        except EOFError:
            print('Bons estudos!')
            break

        if option_chosen == 1:
            print(f'p(x) + q(x) = {p + q}\n')

        elif option_chosen == 2:
            print(f'p(x) * q(x) = {p * q}\n')

        elif option_chosen == 3:
            print('Grau de qual polinômio?')
            for i, name in enumerate(names):
                print(f'[{i + 1}] {name}(x)')

            polynomial_chosen = int(input())
            print(f'O grau de {names[polynomial_chosen - 1]}(x) é {polynomials[names[polynomial_chosen - 1]].get_degree()}')

        elif option_chosen == 4:
            print('Calcular qual polinômio?')
            for i, name in enumerate(names):
                print(f'[{i + 1}] {name}(x)')

            polynomial_chosen = int(input())
            value_input = float(input('Insira um valor de x para avaliar o polinômio: '))

            name = names[polynomial_chosen - 1]
            pol = polynomials[name]
            print(f'{name}({value_input}) = {pol(value_input)}')

        # elif option_chosen == 5:
        #     pass

        print('\n')
