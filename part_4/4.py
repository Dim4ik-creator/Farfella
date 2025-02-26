"""4. В списке все элементы различны. Поменяйте местами минимальный и максимальный
элемент этого списка."""
n = int(input("Введите длину списка: "))
l = []
for i in range(n):
    l.append(int(input("Введите элемент списка: ")))
print("Исходный список:\n", l)
min_index = l.index(min(l))
max_index = l.index(max(l))
l[min_index], l[max_index] = l[max_index], l[min_index]
print("Изменённый список:\n",l)