ages = [0] * 5
heights = [0.0] * 5

for i in range(5):
    age = int(input('Insira sua idade: '))
    height = float(input('Insira sua altura: '))
    ages[i] = age
    heights[i] = height

print('idades: ', end='')
print(*ages[::-1])
print('alturas: ', end='')
print(*heights[::-1])
