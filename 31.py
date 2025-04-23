list = []

a = int(input('Введите начальный индекс: '))
b = int(input('Введите конечный индекс: '))

for i in range (13):
    item = int(input('Введите элемент списка'))
    list.append(item)

for i in range(a, b+1):
    list[i] = 0

print(list)
