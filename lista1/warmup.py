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


states = [
    State('Santa Catarina', 'SC', [City('Florianópolis', 537213), City('Blumenau', 361855)]),
    State('Minas Gerais', 'MG', [City('Belo Horizonte', 2315560), City('Ouro Preto', 74824)]),
    State('Pernambuco', 'PE', [City('Recife', 1488920), City('Petrolina', 386786)])
]

for state in states:
    print(f'Estado: {state.name}, {state.accronym}')
    print(f'População total: {state.population_count} pessoas')
    
    print('Cidades:')
    for city in state.view_cities():
        print(f'\t{city.name}: {city.population_count} pessoas')

    print('\n')


# 8
import math
class Coordinate:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def distance_to(self, coordinate):
        delta_x = self.__x - coordinate.x
        delta_y = self.__y - coordinate.y

        return math.sqrt(abs(delta_x) ** 2 + abs(delta_y) ** 2)

    def get_coordinates(self):
        return f'({self.__x}, {self.__y})'

    def get_coordinates_polar(self):
        magnitude = self.distance_to(Coordinate(0, 0))
        angle = math.degrees(math.atan(self.__y / self.__x))

        return f'{magnitude}∠{angle:.2f}°'

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


coord1 = Coordinate(3, 4)
coord2 = Coordinate(-12, -16)

print(f'distance from {coord1.get_coordinates()} to {coord2.get_coordinates()} is {coord1.distance_to(coord2)}')
print(f'{coord1.get_coordinates()} is {coord1.get_coordinates_polar()} in polar form')


# 9
class Rectangle:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def area(self):
        return self.__base * self.__height

    def perimeter(self):
        return 2 * (self.__base + self.__height)

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, new_base):
        if new_base >= 0:
            self.__base = new_base

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if new_height >= 0:
            self.__height = new_height


class Square:
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2

    def perimeter(self):
        return 4 * self.__size
    
    def diagonal(self):
        return self.__size * math.sqrt(2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        if new_size >= 0:
            self.__size = new_size


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        self.__radius = new_radius


