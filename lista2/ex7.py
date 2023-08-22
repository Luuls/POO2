numbers = [int(n) for n in input('Insira 5 números inteiros separados por espaço: ').split()]

numbers_sum = 0
numbers_product = 1
for number in numbers:
    numbers_sum += number
    numbers_product *= number

print(f'soma: {numbers_sum}, multiplicação: {numbers_product}')
print(*numbers, sep=', ')
