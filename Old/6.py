matrix = [
    [4, 2, 5, 4],
    [6, 1, 7, 2],
    [2, 4, 5, 6]
]
# Вивести максимальний елемент матриці
current_max = 0
current_min = float('inf')

for row in matrix:
    for number in row:
        if number > current_max:
            current_max = number

        if number < current_min:
            current_min = number

print(current_max)
print(current_min)
