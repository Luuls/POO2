numbers = [0] * 10

for i in range(10):
    numbers[i] = int(input('Insira um número: '))

result = 0
for number in numbers:
    result += number ** 2

print(result)
