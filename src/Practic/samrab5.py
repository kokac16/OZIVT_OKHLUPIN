class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

square1 = Square(5)
circle1 = Circle(3)

print(f"Площадь квадрата: {square1.area()}") 
print(f"Площадь круга: {circle1.area()}")  
