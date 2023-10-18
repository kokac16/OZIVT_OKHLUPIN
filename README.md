Отчет по Теме #2 выполнил(а):
- Охлупин Константин Алексеевич
- ИВТ-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | + |
| Задание 7 | + | + |
| Задание 8 | + | + |
| Задание 9 | + | + |
| Задание 10 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа 
### 1) Выведите в консоль три строки. Первая – любое число. Вторая – любое число в виде строки. Третья – любое число с плавающей точкой.

```python
print(123)
print('123')
print(1.23)
```
### Результат.
![ex1](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Lab/1.png)

## Выводы
В данном коде я понял что принт выводит.


### 2) Выведите в консоль три строки. Первая - результат сложения или вычитания минимум двух переменных типа int. Вторая - результат сложения или вычитания минимум двух переменных типа float. Третья - результат сложения или вычитания минимум двух переменных типа int и float.

```python
print(2000 - 1000)
print(1.4 + 2.3)
print(3 + 3.5 + 13 - 10)
```

### Результат.
![ex2](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Lab/two.png)

## Выводы
Этот код выполняет математические операции с использованием базовых математических операторов, таких как + и -


### 3) Выведите в консоль три строки. Первая - обычная строка. Вторая - F строка с использованием заранее объявленной переменной. Третья - сложите две или более строк в одну.

```python
print ("Hello, world!")

world = "World"
print(f"Hello, {world}!")

one = "Hello, "
two = "world!"
print(one + two)
```

### Результат.
![ex3](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Lab/three.png)

## Выводы
В данном коде мы узнали разные способы вывода предложения


### 4) Выведите в консоль три строки. Первая – трансформация любого типа переменной в bool.  Вторая – трансформация любого типа переменной в float или int. Третья – трансформация любого типа переменной в str.

```python
one = "Hello"
print(bool(one))

two = 233
print(float(two))

three = None
print(str(three))
```
### Результат.
![ex4](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Lab/2.png)

### Выводы
Итак, код выполняет преобразования различных типов данных и выводит результаты.


### 5) Присвойте трем переменным различные значения, воспользовавшись функцией input()

```python
one = input("one: ")
two = input("two: ")
three = input("three: ")
print(one, two, three)
```

### Результат.
![ex5](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Lab/3.png)

### Выводы
Код выводит введенные пользователем значения с помощью print(). Таким образом, пользователю предлагается ввести три значения, и после их ввода они выводятся на экран.


### 6) Создайте две любые числовые переменные и выполните над ними несколько математических операций: возведение в степень, обычное деление, целочисленное деление, нахождение остатка от деления. При желании вы можете проверить как работают эти вычисления с разными типами данных, например, сначала создать две переменные int, затем создать две переменные float и наконец создать переменные типа int и float и провести над ними операции, прописанные выше.

```python
a = 12
b = 14
print("Степень:", a ** b)
print("Деление:", a / b)
print("Деление целым числом:", a // b)
print("Остаток от деления:", a % b)
```

### Результат.
![ex6](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Lab/4.png)

### Выводы
Код выполняет различные операции с числами a и b и выводит результат каждой из них.


### 7) Создайте любую строковую переменную и произведите над ней математическое действие умножение на любое число.

```python
line = "Helloo Mikhail!  "
print(line * 8)
```

### Результат.
![ex7](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Lab/5.png)

### Выводы
Умножаем (вводим) количество раз вывода переменной


### 8) Посчитайте сколько раз символ ‘o’ встречается в строке ‘Hello World’.

```python
sentence = "Hellooooo Woooorld"
print(sentence.count("o"))
```

### Результат.
![ex8](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Lab/6.png)

### Выводы
Считам количество буковок "о", count - считать


### 9) Напишите предложение ‘Hello World’ в две строки. Написанная программа должна занимать одну строку в редакторе кода.

```python
print("Hello\nWorld")
```

### Результат.
![ex9](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Lab/7.png)

### Выводы
перенос на новую строку с помощью \n


### 9) Создайте любую строковую переменную и произведите над ней математическое действие умножение на любое число.

```python
print("Hello\nWorld")
```

### Результат.
![ex9](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Lab/7.png)

### Выводы
перенос на новую строку с помощью \n


### 10) Из предложения ‘Hello World’ выведите в консоль только 2 символ, а затем выведите слово ‘Hello’

```python
st = "Hello World"
print(st[1])
print(st[:5])
```

### Результат.
![ex10](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Lab/8.png)

### Выводы
код выводит символ "e" и подстроку "Hello". Выводит подстроку строки st от начала (индекс 0) до индекса 5



## Самостоятельная работа 
### 1) Выведите в консоль булевую переменную False, не используя слово False в строке или  изначально присвоенную булевую переменную. Программа должна занимать не более двух строк редактора кода.

```python
print(bool(0))
```
### Результат.
![ex1](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Practic/1.png)

## Выводы
В данном случае, значение 0 является ложным, поэтому код выведет False.


### 2) Присвоить значения трем переменным и вывести их в консоль, используя только две строки редактора кода

```python
a, b, c = 1, 2, 3
print(a, b, c)
```
### Результат.
![ex2](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Practic/2.png)

## Выводы
Этот код присваивает значения 1, 2 и 3 переменным a, b и c соответственно, а затем выводит их на экран с помощью функции print


### 3) Реализуйте ввод данных в программу, через консоль, в виде только целых чисел (тип данных int). То есть при вводе буквенных символов в консоль, программа не должна работать. Программа должна занимать не более двух строк редактора кода.

```python
one  = input("Ну тут типа пиши число: ")
print(one)
```
### Результат.
![ex3](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Practic/3.png)

## Выводы
Запрашиваем у пользователя ввод числа с помощью функции input и выводит введенное значение на экран с помощью функции print


### 4) Создайте только одну строковую переменную. Длина строки должна не превышать 5 символов. На выходе мы должны получить строку длиной не менее 16 символов. Программа должна занимать не более двух строк редактора кода.

```python
L = "py "

print(L * 20)
```
### Результат.
![ex4](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Practic/4.png)

## Выводы
Вывели чуть больше чем 16 символов)


### 5) Создайте три переменные: день (тип данных - числовой), месяц (тип данных - строка), год (тип данных - числовой) и выведите в консоль текущую дату в формате: “Сегодня день месяц год. Всего хорошего!” используя F строку и оператор end внутри print(), в котором вы должны написать фразу “Всего хорошего!”. Программа должна занимать не более двух строк редактора кода.

```python
day, month, year = 17, "октябрь", 2023
print(f"Сегодня {day} {month} {year}.", end=" Всего хорошего!")
```
### Результат.
![ex5](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Practic/5.png)

## Выводы
Код создает строку с текущей датой, месяцем и годом, и выводит ее, а затем добавляет "Всего хорошего!" без перевода на новую строку.


### 6) В предложении ‘Hello World’ вставьте ‘my’ между двумя словами. Выведите полученное предложение в консоль в одну строку. Программа должна занимать не более двух строк редактора кода.

```python
my = "my"
print(f"Привет, {my}, World!")
```
### Результат.
![ex6](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Practic/6.png)

## Выводы
Значение переменной my вставлено в строку, и она выводится на экран с приветствием.


### 7) Узнайте длину предложения ‘Hello World’, результат выведите в консоль. Программа должна занимать не более двух строк редактора кода.

```python
a = "Hello World!"
print(len(a))
```
### Результат.
![ex7](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Practic/7.png)

## Выводы
КОод считает количество символов, и выыводит значение на экран


### 8) Переведите предложение ‘HELLO WORLD’ в нижний регистр. Программа должна занимать не более двух строк редактора кода.

```python
text = 'HELLO WORLD'.lower()
print(text)
```
### Результат.
![ex8](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Practic/8.png)

## Выводы
Lower - переделывает капс текст в нижний регистр


### 9) Самостоятельно придумайте задачу по проходимой теме и решите ее. Задача должна быть связанна со взаимодействием с числовыми значениями.

```python
#Дана строка Zadacha, проделайте математическое вычесление степени случайных чисел, по итогу используя их значение как павторение данной строки
text = "Zadacha"
a, b = 4, 5
c = (a ** b)
print(text * c)
```
### Результат.
![ex9](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Practic/9.png)

## Выводы
Код повторяет строку "Zadacha" 1024 раз и выводит ее на экран.


### 10) Самостоятельно придумайте задачу по проходимой теме и решите ее. Задача должна быть связанна со взаимодействием с числовыми значениями.

```python
#НАпишите программу для вввода предложения и подсчета слов в нём
input_string = input("Введите строку: ")
words = input_string.split()
word_count = len(words)
print(f"Количество слов в строке: {word_count}")
```
### Результат.
![ex10](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/Theme_2/pic/Practic/10.png)

## Выводы
Код запрашивает у пользователя ввести строку, разбивает ее на слова, вычисляет количество слов и выводит количество слов на экран.


## Общий вывод по теме
- Комментарии в Python представляют собой важный инструмент для улучшения читаемости и понимания кода.
- Функция print() в Python - это инструмент для вывода текста и значений переменных на консоль или в файл.
- Типы переменных определяются автоматически. Основные типы: числа, строки, списки, кортежи, словари, множества, булев тип. Это делает Python гибким для разных задач.
- NoneType в Python используется при определении переменных для задания начального значения, которое можно изменить позже.
- F-строки в Python предоставляют возможность создавать строки, в которых можно вставлять значения переменных и выражений, вычисляемых во время выполнения программы.
- Для ввода данных через консоль в Python используется функция input(). Однако, для дальнейшей работы с этими данными, их часто записывают в переменную.





