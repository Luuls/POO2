from abc import ABC, abstractmethod
class Series(ABC):
    def __init__(self, cache: dict[int, int] = {}):
        self.__cache = cache

    def get_cache(self) -> dict[int, int]:
        return self.__cache

    @abstractmethod
    def __call__(self, n: int) -> int: ...


class Fibonacci(Series):
    def __init__(self):
        Series.__init__(self, {0: 1, 1: 1})

    def __call__(self, n: int) -> int:
        if n < 0:
            raise ValueError('Can not calculate fibonacci term for n < 0')

        cache = self.get_cache()
        if n in cache:
            return cache[n]

        return self(n - 2) + self(n - 1)


fibo = Fibonacci()
print(fibo(10))
