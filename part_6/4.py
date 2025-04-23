"""4. Среди 10 чисел найти максимум и заменить его на среднее арифметическое
положительных элементов."""
def average(l):
    return sum(l) / 10



l = [int(input("Введите элемент списка: ")) for i in range(10)]
l[l.index(max(l))] = average(l)
print(l)