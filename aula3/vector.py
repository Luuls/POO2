from typing import Iterable, overload


class Vector:
    @overload
    def __init__(self, *elements):
        self.__elements = list(elements)
        self.__size = len(self.__elements)

    @overload
    def __init__(self, elements: Iterable):
        self.__elements = elements
        self.__size = len(self.__elements)

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, new_elements):
        self.__elements = new_elements
        self.__size = len(self.__elements)

    @property
    def size(self):
        return self.__size

    @classmethod
    def from_list(cls, elements):
        return cls(*elements)

    def product_by_scalar(self, value):
        for i in range(self.__size):
            self.__elements[i] *= value

    def __add__(self, other):
        if self.__size != other.size:
            raise BufferError

        new_vector = [0] * self.__size
        for i, (this_element, other_element) in enumerate(zip(self.__elements, other.elements)):
            new_vector[i] = this_element + other_element

        return Vector.from_list(new_vector)

v = Vector.from_list([1, 2, 3])
print(v.elements)
v2 = Vector(4, 5, 6)
print(v2.elements)
print(f'{v.elements} + {v2.elements} = {(v + v2).elements}')
