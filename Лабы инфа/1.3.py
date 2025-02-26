a,b,c = int(input('Введите сторону a: ')), int(input('Введите сторону b: ')), int(input('Введите сторону c: '))
# if a+b>c and a+c>b and b+c>a: print(a+b+c)
# else: print('Треугольника не существует!')
print(a+b+c) if a+b>c and a+c>b and b+c>a else print('Треугольника не существует!')