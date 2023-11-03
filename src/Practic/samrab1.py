import os
from collections import Counter

file_path = 'statya.doc'

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
    words = text.split()
    word_count = len(words)
    most_common_word, most_common_word_count = Counter(words).most_common(1)[0]

print(f'Количество слов в файле: {word_count}')
print(f'Самое часто встречающееся слово: "{most_common_word}" (встречается {most_common_word_count} раз)')
