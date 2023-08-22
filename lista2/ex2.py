numbers = [0.0] * 10

for i in range(10):
    numbers[i] = float(input('Insira um número: '))

for i in range(10):
    print(numbers[-(i + 1)])
