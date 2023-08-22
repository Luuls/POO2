vogals = {'a', 'e', 'i', 'o', 'u'}

word = input('Insira uma palavra de 10 letras: ')
consonants = []
for char in word:
    if char not in vogals:
        consonants.append(char)

print(f'{len(consonants)} consoantes: ', end='')
print(*consonants, sep=', ')
