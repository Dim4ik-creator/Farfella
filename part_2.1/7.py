byte = int(input("Введите объем информации в байтах:"))
kbyte = byte / 1024
mbyte = kbyte / 1024
gbyte = mbyte / 1024
print(f"Объем информации в килобайтах: {kbyte}")
print(f"Объем информации в мегабайтах: {mbyte}")
print(f"Объем информации в гигабайтах: {gbyte}")