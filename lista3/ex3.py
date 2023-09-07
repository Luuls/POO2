students: dict[str, list[float]] = {}
while True:
    name = input('Insira o nome do aluno (ou insira nada para concluir): ')
    if not name:
        break

    grades = [float(x) for x in input(f'Insira as duas notas do aluno {name} separadas por espaço:\n').split()]
    students[name] = grades

print('\n')
for name, grades in students.items():
    grade_sum = 0
    for grade in grades:
        grade_sum += grade

    average = grade_sum / len(grades)

    print(f'A média de {name} foi de {average}')
