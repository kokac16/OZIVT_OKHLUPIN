from datetime import datetime
from math import sqrt

# Импортируем необходимые модули: `datetime` для работы с временем и `sqrt` из модуля `math` для вычисления квадратного корня.

def main(**kwargs):
    # Определяем функцию `main`, которая принимает произвольное количество именованных аргументов (**kwargs).
    
    for key in kwargs.items():
        # Начинаем цикл, перебирая элементы в переданных аргументах. `kwargs.items()` возвращает пары (ключ, значение).
        
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        # Для каждой пары (ключ, значение) вычисляем значение по формуле длины вектора: sqrt(x^2 + y^2).
        
        print(result)
        # Выводим результат на экран.
        
if __name__ == '__main__':
    # Проверяем, выполняется ли скрипт напрямую (а не импортируется в другой скрипт).

    start_time = datetime.now()
    # Записываем текущее время до выполнения функции в переменную `start_time`.
    
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    # Вызываем функцию `main` с пятью наборами координат, передаваемыми в виде именованных аргументов.
    
    time_costs = datetime.now() - start_time
    # Вычисляем время, затраченное на выполнение функции, вычитая начальное время из текущего времени.
