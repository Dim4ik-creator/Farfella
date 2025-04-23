"""6. Заменить три последних символа у слов, больших определенной длины."""


def replace_last_three(text, min_length, replacement='...'):
    words = text.split()
    modified_words = [
        word[:-3] + replacement if len(word) > min_length else word
        for word in words
    ]
    return ' '.join(modified_words)


s = input("Введите строку: ")
n = int(input("Введите определенную длину: "))
print(replace_last_three(s,n))