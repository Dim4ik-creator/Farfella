"""3. Выведите все элементы списка с четными индексами."""
n = int(input("Введите длину списка: "))
l = []
for i in range(n):
    element = int(input("Введите элемент списка: "))
    if i % 2 == 0:
        l.append(element)
print(*l)