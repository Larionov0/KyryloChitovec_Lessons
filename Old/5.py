matrix = [
    [1, 2, 5, 4],
    [6, 1, 7, 2],
    [8, 4, 5, 6]
]
# Вивести суму елементів матриці
sum_ = 0

for row in matrix:
    for number in row:
        sum_ += number

# i = 0
# while i < len(matrix):
#     j = 0
#     while j < len(matrix[i]):
#         sum_ += matrix[i][j]
#         j += 1
#     i += 1


print(sum_)
