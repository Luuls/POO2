racers: dict[str, list[float]] = {}

best_lap_time: float
best_lap_racer_name: str
best_lap_number: int
for i in range(6):
    name = input(f'Insira o nome do corredor {i + 1}: ')
    racers[name] = []
    time: float
    times_sum = 0
    for lap in range(10):
        time = float(input(f'Insira o tempo, em segundos, da {lap + 1}ª volta de {name}: '))
        times_sum += time
        racers[name].append(time)

    best_lap_time = time
    best_lap_number = 10
    best_lap_racer_name = name

    min_average = times_sum / len(racers[name])
    winner_name = name

for racer_name, times in racers.items():
    times_sum = 0
    for i, time in enumerate(times):
        times_sum += time

        if time < best_lap_time:
            best_lap_time = time
            best_lap_number = i + 1
            best_lap_racer_name = racer_name

    average = times_sum / len(racers[racer_name])
    if average < min_average:
        min_average = average
        winner_name = racer_name

print(f'A melhor volta foi de {best_lap_racer_name.capitalize()}, sendo {best_lap_time:.2f} na {best_lap_number} volta!')
print(f'O vencedor foi {winner_name.capitalize()}!')
