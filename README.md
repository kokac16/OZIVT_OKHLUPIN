Отчет по Теме #7 выполнил(а):
- Охлупин Константин Алексеевич
- ИВТ-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |  |
| Задание 7 | + |  |
| Задание 8 | + |  |
| Задание 9 | + |  |
| Задание 10 | + |  |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа 
### 1) Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

```python
# Создаем текстовый файл и записываем в него две строки
with open('molodoy_white.txt', 'w') as file:
    file.write('listen to\n')
    file.write('MUSIC\n')

print('Текстовый файл создан и заполнен.')
file.close()
```
### Результат.
![ex1](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Lab/71.png)

## Выводы
with open('molodoy_white.txt', 'w') as file: - Эта строка открывает файл с именем 'molodoy_white.txt' в режиме записи ('w'). Файл будет создан, если его не существует, и любое существующее содержимое будет заменено.
file.write('listen to\n') - Записывает строку 'listen to' в открытый файл, а символ '\n' представляет конец строки, обеспечивая переход на новую строку.
file.write('MUSIC\n') - Записывает строку 'MUSIC' в файл, также завершая строку символом новой строки.
print('Текстовый файл создан и заполнен.') - Выводит сообщение в консоль, указывая, что текстовый файл был создан и заполнен.


### 2) Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию

```python
f = open('molodoy_white.txt', 'r')
print(f.readline())
f.close()
```

### Результат.
![ex2](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Lab/72.png)

## Выводы
f = open('molodoy_white.txt', 'r') - Эта строка открывает файл 'molodoy_white.txt' в режиме чтения ('r') и связывает его с переменной f.
print(f.readline()) - Считывает первую строку из открытого файла с помощью функции readline() и выводит её содержимое на экран.

### 3) Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('molodoy_white.txt', 'r')
print(f.readlines())
f.close()
```

### Результат.
![ex3](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Lab/73.png)

## Выводы
print(f.readlines()) - Считывает все строки из открытого файла с помощью функции readlines() и выводит их в виде списка.


### 4) Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('molodoy_white.txt') as f:
    print(f.readlines())
```
### Результат.
![ex4](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Lab/74.png)

### Выводы
print(f.readlines()) - Считывает все строки из открытого файла с помощью функции readlines() и выводит их в виде списка.


### 5) Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open(). 

```python
with open('molodoy_white.txt') as f:
    for line in f:
        print(line)
```

### Результат.
![ex5](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Lab/75.png)

### Выводы
for line in f: - Итерируется по каждой строке в файле, применяя цикл for, где line представляет текущую строку.


### 6) Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались. 

```python
with open('molodoy_white.txt', '+a') as f:
    f.write('\nI SAY')

with open ('molodoy_white.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

### Результат.
![ex6](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Lab/76.png)

### Выводы
with open('molodoy_white.txt', '+a') as f: - Этот контекстный менеджер открывает файл 'molodoy_white.txt' в режиме добавления ('+a'), что позволяет как читать, так и записывать в файл. С этим режимом файл не будет перезаписан, а данные будут добавлены в конец файла.
f.write('\nI SAY') - Записывает строку '\nI SAY' в файл, добавляя её в конец файла.
with open ('molodoy_white.txt', 'r') as f: - Этот контекстный менеджер открывает тот же файл 'molodoy_white.txt' в режиме чтения ('r').
result = f.readlines() - Считывает все строки из файла с помощью функции readlines() и сохраняет их в переменной result в виде списка строк.


### 7) Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле. 

```python
lines = ['one', 'two', 'three']
with open('molodoy_white.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

### Результат.
![ex7](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Lab/77.png)

### Выводы
lines = ['one', 'two', 'three'] - Создает список строк lines с элементами 'one', 'two' и 'three'.
for line in lines: - Итерируется по каждой строке в списке lines.
f.write('\nCycle run ' + line) - Записывает в файл строку, которая начинается с '\nCycle run ' и добавляет текущий элемент line из списка lines.


### 8) Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory

```python

import os

def print_docs (directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Пanka {catalog[0]} содержит:')
    print (f'Диpekтоpии: {", ".join([folder for folder in catalog [1]])}') 
    print(f'aйлы: {", ".join([file for file in catalog[2]])}') 
    print('-'* 40)
    
print_docs('C:\ProjectWorkProgram\GAME\Wolf')
```

### Результат.
![ex8](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Lab/78.png)

### Выводы
import os - Импортирует модуль os для работы с файловой системой.
def print_docs(directory): - Определяет функцию print_docs, которая принимает путь к директории (directory) в качестве аргумента.
all_files = os.walk(directory) - Использует функцию os.walk() для получения списка всех файлов и подкаталогов в указанной директории.
for catalog in all_files: - Итерируется по результатам os.walk(), где catalog представляет информацию о каждом каталоге в директории.
print(f'Папка {catalog[0]} содержит:') - Выводит имя текущего каталога.
print (f'Директории: {", ".join([folder for folder in catalog[1]])}') - Выводит список подкаталогов в текущем каталоге.
print(f'Файлы: {", ".join([file for file in catalog[2]])}') - Выводит список файлов в текущем каталоге.
print('-' * 40) - Выводит разделительную линию после каждой информации о каталоге.
print_docs('C:\ProjectWorkProgram\GAME\Wolf') - Вызывает функцию print_docs с указанным путем к директории для анализа содержимого.


### 9) Документ «input.txt» содержит следующий текст: Приветствие Спасибо Извините Пожалуйста До свидания Ты готов? Как дела? С днем рождения! Удача! Я тебя люблю. Требуется реализовать функцию, которая выводит слово, имеющеемаксимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных

```python
def longest_words (file):
    with open(file, encoding='utf-8') as f: 
        words = f.read().split()
        max_length= len(max(words, key=len)) 
        for word in words:
            if len(word) == max_length: sought_words = word
        if len(sought_words) == 1: 
            return sought_words[0]
        return sought_words
print(longest_words('input.txt'))
```

### Результат.
![ex9](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Lab/79.png)

### Выводы
def longest_words(file): - Определяет функцию longest_words, которая принимает имя файла (file) в качестве аргумента.
with open(file, encoding='utf-8') as f: - Открывает указанный файл в режиме чтения с указанной кодировкой 'utf-8' с использованием контекстного менеджера.
words = f.read().split() - Считывает содержимое файла, разделяет его на слова и сохраняет их в список words.
max_length = len(max(words, key=len)) - Находит длину самого длинного слова в списке words.
for word in words: - Итерируется по словам в списке.
if len(word) == max_length: sought_words = word - Если длина текущего слова равна максимальной длине, сохраняет это слово в переменной sought_words.
if len(sought_words) == 1: - Проверяет, если sought_words содержит только одно слово.
return sought_words[0] - Если sought_words содержит одно слово, возвращает это слово.
return sought_words - Если sought_words содержит несколько слов, возвращает их в виде списка.


### 10) Требуется создать csv-файл «rows_300.csv» со следующими солбцами:

```python
import csv
import datetime
import time
with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f: 
    writer = csv.writer(f)
    writer.writerow(['No', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат.
![ex10](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Lab/710.png)

### Выводы
with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f: - Открывает файл 'rows_300.csv' для записи в режиме записи ('w') с указанной кодировкой 'utf-8'. Опция newline='' используется для корректной записи строк в CSV-файл.
writer = csv.writer(f) - Создает объект writer для записи данных в файл f.
writer.writerow(['No', 'Секунда ', 'Микросекунда']) - Записывает заголовок CSV-файла с указанными названиями столбцов.
for line in range(1, 301): - Начинает цикл, который будет выполняться 300 раз (от 1 до 300).
writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond]) - Записывает в файл текущее значение номера (line), текущую секунду и текущую микросекунду из объекта datetime.datetime.now().
time.sleep(0.01) - Делает паузу в 0.01 секунды перед следующей итерацией цикла.



## Самостоятельная работа 
### 1) Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация. 

```python
import os
from collections import Counter

file_path = 'statya.doc'

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
    words = text.split()
    word_count = len(words)
    most_common_word, most_common_word_count = Counter(words).most_common(1)[0]

print(f'Количество слов в файле: {word_count}')
print(f'Самое часто встречающееся слово: "{most_common_word}" (встречается {most_common_word_count} раз)')
```
### Результат.
![ex1](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Practic/71.png)

## Выводы
from collections import Counter - Импортирует класс Counter из модуля collections для подсчёта элементов в списке.
file_path = 'statya.doc' - Устанавливает путь к файлу 'statya.doc'.
with open(file_path, 'r', encoding='utf-8') as file: - Открывает файл 'statya.doc' для чтения в режиме 'r' с указанной кодировкой 'utf-8'.
text = file.read() - Считывает содержимое файла в переменную text.
words = text.split() - Разбивает текст на слова и сохраняет их в список words.
word_count = len(words) - Определяет общее количество слов в файле.
most_common_word, most_common_word_count = Counter(words).most_common(1)[0] - Использует Counter для определения наиболее часто встречающегося слова и его количества в тексте.


### 2) У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу дляучета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные вконсоль.  Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
import csv

# Путь к файлу CSV
csv_file_path = 'ras-hod.csv'

while True:
    print("1. Ввести расходы")
    print("2. Вывести существующие расходы")
    
    choice = input("Выберите действие (1/2): ")

    if choice == '1':
        category = input("Категория: ")
        amount = input("Сумма: ")

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([category, amount])

        print("Расходы успешно добавлены.")

    elif choice == '2':
        print("Существующие расходы:")
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f'Category: {row[0]}, Amount: {row[1]}')
```
### Результат.
![ex2](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Practic/72.png)

## Выводы
csv_file_path = 'ras-hod.csv' - Устанавливает путь к файлу CSV, в котором будут храниться данные о расходах.
while True: - Запускает бесконечный цикл для предоставления пользователю опции ввода расходов или вывода существующих расходов.
Пользователь может выбрать действие, вводя '1' для ввода новых расходов или '2' для вывода существующих расходов.
Если пользователь выбирает '1', то программа запрашивает у него категорию расходов и сумму. Затем записывает эту информацию в файл CSV.
Если пользователь выбирает '2', программа выводит существующие расходы, считывая их из файла CSV и выводя их на экран.


### 3) Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. • Текст в файле: Beautiful is better than ugly.Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. • Ожидаемый результат: Input file contains: 108 letters 20 words 4 lines

```python

with open('latinica.txt', 'r', encoding='utf-8') as file:
    text = file.read()

letter_count = sum(1 for char in text if char.isalpha())
word_count = len(text.split())
line_count = len(text.splitlines())

print(f'Количество букв латинского алфавита: {letter_count}')
print(f'Число слов: {word_count}')
print(f'Число строк: {line_count}')

```
### Результат.
![ex3](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Practic/73.png)

## Выводы
letter_count = sum(1 for char in text if char.isalpha()) - Подсчитывает количество букв латинского алфавита в тексте.
word_count = len(text.split()) - Подсчитывает количество слов в тексте.
line_count = len(text.splitlines()) - Подсчитывает количество строк в тексте.


### 4) Напишите программу, которая получает на вход предложение,выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра:

```python
forbidden_words = []
with open('zapret_slov.txt', 'r', encoding='utf-8') as file:
    forbidden_words = file.read().split()

sentence = input("Введите предложение: ")

words = sentence.split()
censored_sentence = []

for word in words:
    lowercase_word = word.lower()
    if lowercase_word in forbidden_words:
        censored_word = '*' * len(word)
        censored_sentence.append(censored_word)
    else:
        censored_sentence.append(word)

censored_text = ' '.join(censored_sentence)
print("Замененное предложение:", censored_text)
```
### Результат.
![ex4](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Practic/74.png)

## Выводы
forbidden_words = [] - Инициализирует пустой список forbidden_words, который будет содержать запрещенные слова.
with open('zapret_slov.txt', 'r', encoding='utf-8') as file: - Открывает файл 'zapret_slov.txt' для чтения в режиме 'r' с указанной кодировкой 'utf-8' с использованием контекстного менеджера. Файл содержит запрещенные слова.
forbidden_words = file.read().split() - Считывает содержимое файла и разделяет его на слова, сохраняя их в список forbidden_words.
sentence = input("Введите предложение: ") - Запрашивает у пользователя ввод предложения.
words = sentence.split() - Разбивает введенное предложение на слова и сохраняет их в список words.
censored_sentence = [] - Инициализирует пустой список censored_sentence, который будет содержать цензурированные слова.


### 5) Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом. Каждая строка представляет собой имя студента, за которым следуют его оценки, разделенные пробелами. Оценки могут быть различной длины. Напишите программу, которая читает этот файл, вычисляет средние оценки для каждого студента и записывает их в новый файл


```python
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
```
### Результат.
![ex5](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_7/pic/Practic/75.png)

## Выводы
parts = line.strip().split(':') - Разбивает строку на части, используя двоеточие как разделитель.
student_name = parts[0] - Получает имя студента.
grades = list(map(int, parts[1].split())) - Получает список оценок студента, разбивая строку с оценками и преобразуя их в целые числа.
average_grade = sum(grades) / len(grades) - Вычисляет средний балл студента.
output_file.write(f"{student_name}: {average_grade:.2f}\n") - Записывает в файл 'students_info.txt' имя студента и его средний балл с округлением до двух знаков после запятой.


## Общий вывод по теме
Открытие файла (open(), close()):
Для открытия файла используется функция open(), которая принимает имя файла и режим доступа (например, "r" для чтения, "w" для записи, "a" для дозаписи и т. д.).
Файлы должны быть закрыты после использования с помощью метода close().
Чтение из файла:
Для чтения данных из файла можно использовать методы readline(), который читает одну строку, и readlines(), который читает все строки и возвращает их в виде списка.
Запись в файл:
Запись в файл осуществляется с помощью метода write(), который принимает строку и записывает её в файл. Режим файла должен быть "w" или "a" для записи.
Управление указателем чтения/записи:
Python автоматически управляет указателем в файле, но вы можете перемещать его с помощью методов seek() и tell(). seek() позволяет установить позицию указателя, а tell() возвращает текущую позицию.
Управление буферизацией:
Python автоматически буферизирует данные при чтении и записи файлов, но вы можете управлять буферизацией, устанавливая параметры buffering при открытии файла.