c = [(int(input("Введите x: ")), int(input("Введите y: "))) for x in range(3)]
if c[0][0] is c[1][0]:
    x = c[2][0]
elif c[0][0] is c[2][0]:
    x = c[1][0]
elif c[1][0] is c[1][0]:
    x = c[0][0]
elif c[0][1] is c[1][1]:
    y = c[2][1]
elif c[0][1] is c[2][1]:
    y = c[1][1]
else:
    y = c[0][1]
print(f"Координаты четвертой вершины: {x, y}")
