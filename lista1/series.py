from abc import ABC, abstractmethod
from math import factorial
class Series(ABC):
    def __init__(self, cache: dict[int, int] = {}):
        self.__cache = cache

    def get_cache(self) -> dict[int, int]:
        return self.__cache

    @abstractmethod
    def __call__(self, n: int) -> int: ...


class Factorial(Series):
    def __init__(self):
        Series.__init__(self, {0: 1})

    def __call__(self, n: int) -> int:
        if n < 0:
            raise ValueError('Can not calculate fibonacci term for n < 0')

        cache = self.get_cache()
        if n in cache:
            return cache[n]

        return self(n - 1) * n


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


class Prime(Series):
    def __init__(self):
        Series.__init__(self, {0: 2})

    def __call__(self, n: int) -> int:
        if n < 0:
            raise ValueError('Can not calculate prime term for n < 0')

        cache = self.get_cache()
        if n in cache:
            return cache[n]

        last_term_cached = max(cache.keys())
        # último primo registrado
        candidate = cache[last_term_cached] + 1
        for i in range(last_term_cached + 1, n + 1):
            while True:
                if self.__is_prime(candidate):
                    cache[i] = candidate
                    candidate += 1
                    break

                candidate += 1

        return cache[n]

    def __is_prime(self, number: int) -> bool:
        divisor = 2
        while divisor ** 2 <= number:
            if number % divisor == 0:
                return False
            
            divisor += 1

        return True


print('FIBONACCI')
fibo = Fibonacci()
for i in range(15):
    print(fibo(i))

print('\nPRIMO')
prime = Prime()
for i in range(15):
    print(prime(i))

print('\nFATORIAL')
factorial = Factorial()
for i in range(15):
    print(factorial(i))
