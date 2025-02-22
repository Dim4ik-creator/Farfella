print(f"Ваш ответ: {len(list(filter(lambda x: x > 0 and x % 2 == 0, [int(input(f"Введите число {x}: ")) for x in range(1,4)])))}")
