"""5. В списке определить количество четных и нечетных элементов."""


def even_and_odd(l):
    even = 0
    odd = 0
    for i in range(len(l)):
        if l[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


n = int(input("Введите размер списка: "))
l = [int(input("Введите элемент списка: ")) for i in range(n)]
even, odd = even_and_odd(l)
print(f"Количество четных элементов:{even}\nКоличество нечетных элементов:{odd}")
