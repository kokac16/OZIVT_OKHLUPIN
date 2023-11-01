
user_input = input("Введите последовательность чисел, разделенных пробелами: ")
numbers = user_input.split()
numbers = [int(num) for num in numbers]
number_list = numbers
number_tuple = tuple(numbers)
print("Список из введенных чисел:", number_list)
print("Кортеж из введенных чисел:", number_tuple)
