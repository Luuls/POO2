numbers = [0] * 5
for i in range(5):
    numbers[i] = int(input('Insira um número: '))

print(*numbers, sep=', ')
