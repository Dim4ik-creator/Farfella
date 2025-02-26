"""1. Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону"""
start = int(input("Введите начальное значение диапазона: "))
end = int(input("Введите конечное значение диапазона: "))
l = []
for meaning in range(start, end + 1):
    l.append(meaning)
for i in range(len(l)):
    print(i)
