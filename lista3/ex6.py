import random

frozensets: dict[frozenset, float] = {}
for i in range(10):
    values = [random.randint(0, 100) for _ in range(30)]
    new_set = frozenset(values)
    frozensets[new_set] = sum(new_set)

for current_set, set_sum in frozensets.items():
    formated_str = '{'
    for number in current_set:
        formated_str += f'{number}, '

    formated_str = formated_str.removesuffix(', ') + '}'
    print(f'A soma dos elementos de {formated_str} é {set_sum}')
