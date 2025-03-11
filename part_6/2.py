"""2. Посчитать количества одинаковых элементов в списке, используя функцию."""
def length(l, n):
    return n - len(set(l))


n = int(input("Введите размер списка: "))
l = [int(input("Введите элемент списка: ")) for i in range(n)]
print(length(l,n))
