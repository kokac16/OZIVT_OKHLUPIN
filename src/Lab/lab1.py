# Создаем текстовый файл и записываем в него две строки
with open('molodoy_white.txt', 'w') as file:
    file.write('listen to\n')
    file.write('MUSIC\n')

print('Текстовый файл создан и заполнен.')
file.close()