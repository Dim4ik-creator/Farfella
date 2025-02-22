"""Среди 10 чисел, вводимых с клавиатуры, найти количество положительных и
отрицательных значений."""
count_plus = 0
count_minus = 0
number = 0
for i in range(10):
    number = int(input("Введите число: "))
    if number > 0:
        count_plus += 1
    else:
        count_minus += 1
print(f"Количество положительных чисел: {count_plus}")
print(f"Количество отрицательных чисел: {count_minus}")