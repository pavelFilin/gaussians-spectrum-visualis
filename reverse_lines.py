with open('input.csv', 'r') as file:
    lines = file.readlines()

# Удаление лишних символов перевода строки и реверс списка
lines = [line.strip() for line in lines]
reversed_lines = lines[::-1]

# Запись результата в файл
with open('output.csv', 'w') as file:
    for line in reversed_lines:
        file.write(line + '\n')