"""2. В массиве 5*5 обнулить главную и побочную диагональ."""
matrix = [[int(input("Введите значение массива: ")) for _ in range(5)] for _ in range(5)]
for i in range(5):
    matrix[i][i] = 0

for i in range(5):
    matrix[i][4 - i] = 0

for row in matrix:
    print(row)