one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_values = [max(one), max(two), max(three)]
min_values = [min(one), min(two), min(three)]

max_values.sort()
min_values.sort()

def calculate(sides):
    a, b, c = sides
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

max_area1 = calculate([max_values[-1], max_values[-2], max_values[-3]])
min_area1 = calculate([min_values[0], min_values[1], min_values[2]])

print("Площадь треугольника с максимальными сторонами:", max_area1)
print("Площадь треугольника с минимальными сторонами:", min_area1)
