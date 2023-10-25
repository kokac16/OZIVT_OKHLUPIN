from FormulaGeron import calculate

try:
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))

    if a > 0 and b > 0 and c > 0:
        area = calculate(a, b, c)
        print(f"Площадь треугольника: {area:.2f}")
    else:
        print("Длины сторон треугольника должны быть положительными числами.")
except ValueError:
    print("Некорректный ввод. Введите числа для длин сторон треугольника.")