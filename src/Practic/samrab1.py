def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Генерация 200 чисел Фибоначчи
fibonacci_sequence = list(fib(200))

# Вывод результатов в консоль
print(fibonacci_sequence[-1])
