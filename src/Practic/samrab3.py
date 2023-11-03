
with open('latinica.txt', 'r', encoding='utf-8') as file:
    text = file.read()

letter_count = sum(1 for char in text if char.isalpha())
word_count = len(text.split())
line_count = len(text.splitlines())

print(f'Количество букв латинского алфавита: {letter_count}')
print(f'Число слов: {word_count}')
print(f'Число строк: {line_count}')
