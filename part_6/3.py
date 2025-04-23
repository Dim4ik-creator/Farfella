"""3. Разделить элементы списка на минимальный элемент."""
def min_list(l):
    mn = float("inf")
    for i in range(len(l)):
        if l[i] < mn:
            mn = l[i]
    return mn


def devide_min(l):
    mn = min_list(l)
    if mn == 0:
        return "Минимальный элемент равен 0, деление невозможно"
    for i in range(len(l)):
        l[i] = l[i] / mn
    return l


n = int(input("Введите размер списка: "))
l = [int(input("Введите элемент списка: ")) for i in range(n)]
print(devide_min(l))
