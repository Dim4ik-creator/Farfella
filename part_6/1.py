"""1. Определить наименьшее общее кратное для чисел а и в."""
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Введите число a:"))
b = int(input("Введите число b:"))

print(f"Наименьшее общее кратное: {abs(a*b) // gcd(a,b)}")