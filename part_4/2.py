"""2. Найти произведение первого, пятого и восьмого положительных элементов массива"""
element = 0
l = []
for i in range(8):
    element = int(input("Введите элемент массива: "))
    l.append(element)
print(l[0] * l[4] * l[7])