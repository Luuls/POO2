students = [[] for _ in range(10)]

for n, student in enumerate(students):
    for i in range(4):
        student.append(float(input(f'Insira a {i + 1}ª nota do {n + 1}° estudante: ')))

grades_gte_7 = 0
for student in students:
    grades_sum = 0.0
    for grade in student:
        grades_sum += grade

    if grades_sum / 4 >= 7:
        grades_gte_7 += 1

print(grades_gte_7)
