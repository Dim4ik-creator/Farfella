"""5. Определить длину самого короткого слова в строке."""
s = input("Введите строку: ")
l = s.split()
min_len_word = 999999999
for word in l:
    if len(word) < min_len_word:
        min_len_word = len(word)
print(min_len_word)