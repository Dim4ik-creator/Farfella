"""Ввести два целых однозначных числа. Программа задаёт вопрос: "Результат
умножения первого числа на второе?" Пользователь должен ввести ответ и увидеть на
экране правильно он ответил или нет. Если нет – показать еще и правильный
результат.
"""
a,b = int(input("Введите первое число:")), int(input("Введите второе число:"))
print("Результат умножения первого числа на второе?")
answer = int(input("Введите ответ:"))
if answer is (a * b):
    print("Верно")
else:
    print("Неверно. Верный ответ:", a * b)