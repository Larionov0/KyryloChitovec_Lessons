matrix = [
    [1, 2, 5, 4],
    [6, 1, 7, 2],
    [8, 4, 5, 6]
]
# Користувач вводить число
# Програма виводить ряд матриці за цим індексом

index = int(input("Введите індекс: "))

j = 0
while j < 4:
    print(matrix[index][j])
    j += 1

# row = matrix[index]
# for number in row:
#     print(number)
