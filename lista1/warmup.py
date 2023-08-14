# 1
class Television:
    def __init__(self):
        self.__is_on = False
        self.__channel = 2


# 2
class Television:
    def __init__(self):
        self.__is_on = False
        self.__channel = 2
        self.__brand: str
        self.__size: int

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        self.__size = new_size

tv1 = Television()
tv1.brand = 'Philco'
tv1.size = 32

tv2 = Television()
tv2.brand = 'Panasonic'
tv2.size = 28

print('tv1')
print(f'brand: {tv1.brand}')
print(f'size: {tv1.size}\n')

print('tv2')
print(f'brand: {tv2.brand}')
print(f'size: {tv2.size}')


# 3 
class Television:
    def __init__(self, channel = 2):
        self.__is_on = False
        self.__channel = channel
        self.__brand: str
        self.__size: int

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        self.__size = new_size

    def channel_up(self):
        self.__channel += 1

    def channel_down(self):
        self.__channel -= 1


# 4
class Television:
    def __init__(self, channel = 2):
        self.__is_on = False

        self.__channel = channel
        self.__min_channel = 1
        self.__max_channel = 99

        self.__brand: str
        self.__size: int

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        self.__size = new_size

    def channel_up(self):
        if self.__channel == self.__max_channel:
            self.__channel = self.__min_channel
            return

        self.__channel += 1

    def channel_down(self):
        if self.__channel == self.__min_channel:
            self.__channel = self.__max_channel
            return

        self.__channel -= 1


# 5
class Television:
    def __init__(self, channel=2, min_channel=2, max_channel=14):
        self.__is_on = False

        self.__channel = channel
        self.__min_channel = min_channel
        self.__max_channel = max_channel

        self.__brand: str
        self.__size: int

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        self.__size = new_size

    def channel_up(self):
        if self.__channel == self.__max_channel:
            self.__channel = self.__min_channel
            return

        self.__channel += 1

    def channel_down(self):
        if self.__channel == self.__min_channel:
            self.__channel = self.__max_channel
            return

        self.__channel -= 1


# 6 (?)


# 7
class City:
    def __init__(self, name, population_count):
        self.__name = name
        self.__population_count = population_count

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def population_count(self):
        return self.__population_count

    @population_count.setter
    def population_count(self, value):
        self.__population_count = value

class State:
    def __init__(self, name, accronym, cities):
        self.__name = name
        self.__accronym = accronym
        self.__cities = cities
        self.__population_count = self.__compute_population()

    def __compute_population(self):
        population_sum = 0
        for city in self.__cities:
            population_sum += city.population_count

        return population_sum

    def view_cities(self):
        """returns a view on cities values"""
        return self.__cities.copy()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def accronym(self):
        return self.__accronym

    @accronym.setter
    def accronym(self, new_accronym):
        self.__accronym = new_accronym

    @property
    def population_count(self):
        return self.__population_count


state1 = State('Santa Catarina', 'SC', [City('Florianópolis', 537213), City('Blumenau', 361855)])
state2 = State('Minas Gerais', 'MG', [City('Belo Horizonte', 2315560), City('Ouro Preto', 74824)])
state3 = State('Pernambuco', 'PE', [City('Recife', 1488920), City('Petrolina', 386786)])

states = [state1, state2, state3]
for state in states:
    print(f'Estado: {state.name}, {state.accronym}')
    print(f'População total: {state.population_count} pessoas')
    
    print('Cidades:')
    for city in state.view_cities():
        print(f'\t{city.name}: {city.population_count} pessoas')

    print('\n')
