def add_two_and_number():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = 2 + number
        print(f"Результат сложения 2 и {number} равен {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

# Тесты
add_two_and_number()  # Ввод корректного числа
add_two_and_number()  # Ввод строки
add_two_and_number()  # Ввод некорректного числа
