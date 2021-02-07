n = 10
m = 12
sym = '-'

matrix = []
i = 0
while i < n:
    row = []
    j = 0
    while j < m:
        row.append(sym)
        j += 1

    matrix.append(row)
    i += 1


# виведення матриці на екран
for row in matrix:  # [4, 2, 5, 4]
    text = '|'
    for el in row:
        text += str(el) + " "
    text = text[:-1] + "|"
    print(text)
