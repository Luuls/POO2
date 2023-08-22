numbers = [0] * 20
evens = []
odds = []
for i in range(20):
    numbers[i] = int(input('Insira um número: '))
    if numbers[i] % 2 == 0:
        evens.append(numbers[i])

    else:
        odds.append(numbers[i])

print(numbers)
print(evens)
print(odds)
