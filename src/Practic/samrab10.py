# Создаем пустой файл
with open('empty_file.txt', 'w') as empty_file:
    pass

# Создаем файл с информацией
with open('data_file.txt', 'w') as data_file:
    data_file.write('Это файл с какой-то информацией')