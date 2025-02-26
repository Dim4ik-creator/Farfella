"""5. Найти среднее арифметическое отрицательных элементов в двумерном списке 7*7.
Заменить на него минимальный элемент."""
matrix = []
for i in range(7):
    row = []
    for j in range(7):
        row.append(int(input()))
    matrix.append(row)

suma = 0
for row in matrix:
    for j in row:
        suma += j

average = suma / 49
min_row, min_col = -1, -1
min_element = -999999999999
for i in range(7):
    for j in range(7):
        if matrix[i][j] < min_element:
            min_element = matrix[i][j]
            min_row, min_col = i, j
matrix[min_row][min_col] = average
print(matrix)
