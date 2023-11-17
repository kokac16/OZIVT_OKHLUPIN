def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            if not content:
                raise Exception("файл пустой")
            else:
                print("Содержимое файла:")
                print(content)
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден")
    except Exception as e:
        print(e)

# Проверяем пустой файл
read_file('empty_file.txt')
print('-------------------')
# Проверяем файл с информацией
read_file('data_file.txt')