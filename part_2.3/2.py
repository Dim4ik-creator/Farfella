"""Найти среднее арифметическое положительных чисел, введенных с клавиатуры. Всего
ввести N различных чисел."""
n = int(input("Введите количество чисел: "))
summa = 0
for i in range(n):
    summa += int(input("Введите положительное число: "))
print(f"Среднее арифметическое положительных чисел: {summa / n}")