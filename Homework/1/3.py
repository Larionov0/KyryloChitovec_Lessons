matrix = [
    [1, 2, 5, 4],
    [6, 1, 7, 0],
    [8, 4, 5, 6]
    ]

while True:
    number = int(input('Type in a number: '))

    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j] == number:
                print(f"Ряд {i}. Стовпець {j}")
            j += 1
        i += 1
