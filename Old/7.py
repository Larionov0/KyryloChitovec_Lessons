matrix = [
    [4, 2, 5, 4],
    [6, 1, 7, 2],
    [2, 4, 5, 6]
]

# виведення матриці на екран
for row in matrix:  # [4, 2, 5, 4]
    text = '|'
    for el in row:
        text += str(el) + " "
    text = text[:-1] + "|"
    print(text)
