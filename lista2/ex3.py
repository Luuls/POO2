grades = [0.0] * 4
for i in range(4):
    grades[i] = float(input(f'Insira a {i}ª'))

grades_sum = 0.0
for grade in grades:
    grades_sum += grade

print(grades_sum / 4)
