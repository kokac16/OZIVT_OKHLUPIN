#Каждая строка представляет собой имя студента, за которым следуют его оценки, разделенные пробелами. Оценки могут быть различной длины. Напишите программу, которая читает этот файл, вычисляет средние оценки для каждого студента и записывает их в новый файл
with open('students.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open('students_info.txt', 'w', encoding='utf-8') as output_file:
    for line in lines:
        parts = line.strip().split(':')
        student_name = parts[0]
        grades = list(map(int, parts[1].split()))
        average_grade = sum(grades) / len(grades)
        output_file.write(f"{student_name}: {average_grade:.2f}\n")

print("Средние оценки успешно записаны в файл 'students_info.txt'.")