def calculate(*args):
   
    if len(args) == 0:
        return 0.0
    
   
    total = sum(args)
    
    
    average = total / len(args)
    
    return average

if __name__ == "__main__":
    
    numbers = []
    while True:
        try:
            num = float(input("Введите число (для завершения введите пустую строку): "))
            numbers.append(num)
        except ValueError:
            if not numbers:
                print("Вы не ввели ни одного числа.")
            else:
                avg = calculate(*numbers)
                print(f"Среднее арифметическое: {avg}")
            break
