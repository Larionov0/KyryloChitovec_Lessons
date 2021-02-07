matrix = [
    [1, 2, 5, 4],
    [6, 1, 7, 2],
    [8, 4, 5, 6]
]
index = int(input("Введіть індекс: "))
j = 0
inf = float('inf')
while j < 4:
    matrix[index][j] = 1
    j += 1


for row in matrix:
    text = '|'
    for el in row:
        text += str(el) + " "
    text = text[:-1] + "|"
    print(text)
