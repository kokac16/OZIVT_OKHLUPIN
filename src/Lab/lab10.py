global result

def rectangle():
    a = float(input("ширина: "))
    b = float(input("Bыcoтa: ")) 
    global result
    result = a * b

def triangle():
    a = float(input("Основание: ")) 
    h = float(input("Bыcoтa: ")) 
    global result
    result = 0.5 * a *h

figure = input("1-прямоугольник, 2-треугольник: ")
if figure == '1': 
    rectangle()
elif figure == '2':
    triangle()
print(f"Плoшадь: {result}")