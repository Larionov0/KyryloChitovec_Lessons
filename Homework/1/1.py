from os import system

matrix = [
    [1, 2, 5, 4],
    [6, 1, 7, 2],
    [8, 4, 5, 6]
]
while True:
    i = int(input("Type row index: "))
    j = int(input("Type column index: "))
    print(matrix[i][j])
    print(" ")
    system('cls')
