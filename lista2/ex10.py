numbers1 = [0] * 10
numbers2 = [0] * 10

for i in range(10):
    numbers1[i] = int(input(f'Insira um número para o vetor 1: '))

for i in range(10):
    numbers2[i] = int(input(f'Insira um número para o vetor 2: '))

intercalated = []
for i in range(10):
    intercalated.append(numbers1[i])
    intercalated.append(numbers2[i])

print(intercalated)

