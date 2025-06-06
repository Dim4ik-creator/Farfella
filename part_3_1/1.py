"""
1. Определить длину строки.
2. Организовать поиск подстроки в строке.
3. Перевести символы нижнего регистра в верхний, а верхнего – в нижний.
4. Разбить строку по разделителю (в качестве разделителя использовать символ пробел).
5. Проверить, состоит ли строка из цифр.
6. Преобразовать строку к верхнему регистру.
7. Первые буквы в словах представить в коде ASCII.
8. Используя методы find и rfind, определить вхождение подстроки "ведром".
9. Используя метод replace, заменить "Том" на "Тим".
10. Используя метод replace с параметром count, заменить символ "о" на "а", но не все
вхождения, а только первые 3 из них."""
string = "Том появился на тротуаре с ведром известки и длинной кистью в руках"
print(f"1. {len(string)}")
print(f"2. {string.index(input("Введите подстроку: "))}")
print(f"3. {string.swapcase()}")
print(f"4. {string.split()}")
print(f"5. {string.isdigit()}")
print(f"6. {string.upper()}")
print(f"7. {[ord(i[0]) for i in string.split()]}")
print(f"8. {string.find("ведром"),string.rfind("ведром")}")
print(f"9. {string.replace("Том","Тим")}")
print(f"10. {string.replace("о","а",3)}")