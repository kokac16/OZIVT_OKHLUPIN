import csv

# Путь к файлу CSV
csv_file_path = 'ras-hod.csv'

while True:
    print("1. Ввести расходы")
    print("2. Вывести существующие расходы")
    
    choice = input("Выберите действие (1/2): ")

    if choice == '1':
        category = input("Категория: ")
        amount = input("Сумма: ")

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([category, amount])

        print("Расходы успешно добавлены.")

    elif choice == '2':
        print("Существующие расходы:")
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f'Category: {row[0]}, Amount: {row[1]}')