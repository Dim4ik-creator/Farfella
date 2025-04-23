"""4. Вводится строка. Необходимо определить в ней проценты прописных (больших) и
строчных (малых) букв"""


def func(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.islower():
            lower_count += 1
        if char.isupper():
            upper_count += 1
    upper_percentage = (upper_count / len(s)) * 100
    lower_percentage = (lower_count / len(s)) * 100
    return f"Процент прописных букв: {upper_percentage:.2f}%\nПроцент строчных букв: {lower_percentage:.2f}%"

s = input("Введите строку: ")
print(func(s))