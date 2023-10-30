Отчет по Теме #5 выполнил(а):
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
### 1) Друзья предложили вам поиграть в игру “найди отличия и убери повторения (версия для программистов)”. Суть игры состоит в том, что на вход программы поступает два множества, а ваша задача вывести все элементы первого, которых нет во втором. А вы как раз недавно прошли множества и знаете их возможности, поэтому это не составит для вас труда

```python
set_1 = {'White', 'Black', 'Red', 'Pink'} 
set_2 = {'Red', 'Green', 'Blue', 'Red'}
print(set_1 - set_2)
```
### Результат.
![ex1](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Lab/41.png)

## Выводы
Код выполняет операцию разности множеств (set difference) между set_1 и set_2. Результат этой операции будет содержать элементы, которые присутствуют в set_1, но отсутствуют в set_2.


### 2) Напишите две одинаковые программы, только одна будет использовать set(), а вторая frozenset() и попробуйте к исходному множеству добавить несколько элементов, например, через цикл.

```python
a = set('abcdefg') 
print(a)
for i in range(1, 5): 
    a.add(i)
print(a)
```

### Результат.
![ex2](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Lab/42.png)

## Выводы
Код создает множество a, исходно содержащее элементы 'a', 'b', 'c', 'd', 'e', 'f' и 'g'. Затем, с использованием цикла for, добавляются элементы от 1 до 4 в множество a

### 3) На вход в программу поступает список (минимальной длиной 2 символа). Напишите программу, которая будет менять первый и последний элемент списка.

```python
def replace(input_list):
    memory = input_list[0] 
    input_list[0] = input_list[-1] 
    input_list[-1] = memory
    return input_list
print (replace([1, 2, 3, 4, 5]))
```

### Результат.
![ex3](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Lab/43.png)

## Выводы
Сохраняет первый элемент списка input_list в переменной memory.
Затем заменяет первый элемент списка input_list на последний элемент списка (input_list[-1]).
Заменяет последний элемент списка input_list на значение, которое было сохранено в переменной memory.
Возвращает измененный список input_list.


### 4) На вход в программу поступает список (минимальной длиной 10 символов). Напишите программу, которая выводит элементы с индексами от 2 до 6. В программе необходимо использовать “срез”.

```python
a = [12, 54, 32, 57, 843, 2346, 765, 75, 25, 234, 756, 23] 

print(a[2:6])
```
### Результат.
![ex4](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Lab/44.png)

### Выводы
од работает с списком a и использует срез (slice) для извлечения подсписка элементов. В данном случае, a[2:6] извлекает элементы с индексами с 2 по 5 (включительно), так как срез задается в формате [начало:конец], где начало включено, а конец исключен.


### 5) Иван задумался о поиске «бесполезного» числа, полученного из списка. Суть поиска в следующем: он берет произвольный список чисел, находит самое большое из них, а затем делит его на длину списка. Студент пока не придумал, где может пригодиться подобное значение, но ищет у вас помощи в реализации такой функции useless().

```python
def useless(lst):
    return max(lst) / len(lst)
print(useless([3, 5, 7, 3, 33]))
print(useless([-12.5, 54, 77.3, 0, -36, 98.2, -63, 21.7, 47, -89.6])) 
print (useless([-25.8, 86, 12.5, -56, 73.2, 0, 43, -91.5, 65.9, -7]))
```

### Результат.
![ex5](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Lab/45.png)

### Выводы
Находит максимальный элемент в списке lst с помощью функции max(lst).
Далее, делим найденное максимальное значение на длину списка lst (количество элементов в списке), которое находится с помощью функции len(lst). Функция useless возвращает максимальный элемент списка lst, разделенный на количество элементов в этом списке.


### 6) Ребята не могут определится каким супергероем они хотят стать. У них есть случайно составленный список супергероев, и вы должны определить кто из ребят будет каким супергероем. Необходимо использовать разделение списков. 

```python
superheroes = ['superman', 'spiderman', 'batman']
nikolay, vasiliy, ivan = superheroes

print('Hиколaй - ', nikolay)
print('Василий -', vasiliy)
print('Иван-', ivan)
```

### Результат.
![ex6](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Lab/46.png)

### Выводы
Определяет список superheroes, который содержит три строки: 'superman', 'spiderman' и 'batman'.
Затем происходит распаковка списка superheroes в три переменные: nikolay, vasiliy и ivan. Каждое значение из списка superheroes присваивается соответствующей переменной.
После распаковки, код выводит имена и их значения в виде трех строк


### 7)  Вовочка, насмотревшись передачи “Слабое звено” решил написать программу, которая также будет находить самое слабое звено (минимальный элемент) и удалять его, только делать он это хочет не с людьми, а со списком. Помогите Вовочке с реализацией программы.

```python
a = [-25.8, 86, 12.5, -56, 73.2, 0, 43, -91.5, 65.9, -7] 
a.sort()
print('Отсортированный список:\n', a)

a.pop(0)
print('Отсортированный список без наименьшего элемента:\n', a)
```

### Результат.
![ex7](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Lab/47.png)

### Выводы
Создает список a, содержащий десять чисел.
Сортирует список a в порядке возрастания с помощью метода sort().
Выводит отсортированный список a.
Удаляет первый элемент (наименьший элемент) из отсортированного списка a с помощью метода pop(0)


### 8) Михаил решил создать большой n-мерный список, для этого он случайным образом создал несколько списков, состоящих минимум из  3, а максимум из 10 элементов и поместил их в один большой список. Он также как и Иван не знает зачем ему это сейчас нужно, но надеется на то, что это пригодится ему в будущем. 

```python
from random import randint

def list_maker():
    a = [randint(1, 100)] * randint(3, 10) 
    return a

if __name__ == '__main__':
    result = []
    for i in range(randint(1, 5)): 
        result.append(list_maker())
    print(result)
```

### Результат.
![ex8](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Lab/48.png)

### Выводы
Создается пустой список result.
Запускается цикл for, который выполняется случайное количество раз от 1 до 5 (включительно), так как randint(1, 5) определяет количество итераций.
На каждой итерации вызывается функция list_maker(), и результат (случайно сгенерированный список) добавляется в список result с помощью метода append().
В конце код выводит список result


### 9) Вы работаете в ресторане и отвечает за статистику покупок, ваша задача сравнить между собой заказы покупателей, которые указаны в разном порядке. Реализуйте функцию superset(), которая принимает 2 множества. Результат работы функции: вывод в консоль одного из сообщений в зависимости от ситуации: 1 - «Супермножество не обнаружено» 2 – «Объект {X} является чистым супермножеством» 3 – «Множества равны» 

```python
def superset (set_1, set_2):
    if set_1 > set_2:
        print(f'Объект {set_1} является чистым супермножеством') 
    elif set_1 == set_2:
        print(f'Множества равны')
    elif set_1 < set_2:
        print(f'Объект {set_2} является чистым супермножеством ')
    else:
        print('Супермножество не обнаружено')
   
if __name__ == '__main__':
    superset({1, 8, 3, 5}, {3, 5})
    superset({1, 8, 3, 5}, {5, 3, 8, 1})
    superset ({3, 5}, {5, 3, 8, 1})
    superset ({90, 100}, {3, 5})
```

### Результат.
![ex9](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Lab/49.png)

### Выводы
Функция `superset` принимает два множества `set_1` и `set_2` и определяет их отношение друг к другу с помощью операторов сравнения.
- Если `set_1` содержит все элементы `set_2` и возможно дополнительные, то выводится сообщение о чистом супермножестве `set_1`.
- Если `set_1` и `set_2` равны, то выводится сообщение о равенстве множеств.
- Если `set_1` содержит некоторые, но не все элементы `set_2`, то выводится сообщение о чистом супермножестве `set_2`.
- Если ни одно из условий не выполняется, выводится сообщение "Супермножество не обнаружено".
Далее, в блоке `if __name__ == '__main__':` функция `superset` вызывается с различными парами множеств для проверки её работы.


### 10) Предположим, что вам нужно разобрать стопку бумаг, но нужно начать работу с нижней, “переверните стопку”. Вам дан произвольный список. Представьте его в обратном порядке. Программа должна занимать не более двух строк в редакторе кода.

```python

my_list = [2, 5, 8, 3]
print(my_list[::-1])
```

### Результат.
![ex10](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Lab/410.png)

### Выводы
my_list[::-1] возвращает копию списка my_list, но с шагом -1, что обращает порядок его элементов. Таким образом, исходный список не изменяется, но выводится его обратный порядок.
print(my_list[::-1]) выводит инвертированный список на экран.



## Самостоятельная работа 
### 1) Ресторан на предприятии ведет учет посещений за неделю при помощи кода работника. У них есть список со всеми посещениями за неделю. Ваша задача почитать: • Сколько было выдано чеков • Сколько разных людей посетило ресторан • Какой работник посетил ресторан больше всех раз

```python

checks = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365, 
         1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666, 
         5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928, 
         5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987, 
         3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]
num_checks = len(checks)

visitors = set(checks)
num_visitors = len(visitors)


worker = max(visitors, key=checks.count)


print("Сколько было выдано чеков:", num_checks)
print("Сколько разных людей посетило ресторан:", num_visitors)
print("Какой работник посетил ресторан больше всех раз:", worker)

```
### Результат.
![ex1](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Practic/41.png)

## Выводы
len(): Эта функция используется для определения длины списка. Например, len(checks) возвращает количество элементов в списке checks, представляющих выданные чеки.
set(): Этот встроенный метод Python используется для создания множества из итерируемого объекта. В данном случае, set(checks) создает множество visitors, удаляя дубликаты из списка checks и сохраняя только уникальные значения.
max(): Эта функция возвращает наибольший элемент из итерируемого объекта или два аргумента сравнения. В данном коде используется max() с параметром key=checks.count, чтобы найти элемент с наибольшим количеством вхождений в список checks. Это позволяет определить работника, который посетил ресторан больше всех раз.


### 2) На физкультуре студенты сдавали бег, у преподавателя физкультуры есть список всех результатов, ему нужно узнать • Три лучшие результата • Три худшие результата • Все результаты начиная с 10 Ваша задача помочь ему в этом.

```python
results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 
           27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

best_results = sorted(results)[:3]

worst_results = sorted(results)[-3:]

above_10_results = [result for result in results if result >= 10]

print("Три лучших результата:", best_results)
print("Три худших результата:", worst_results)
print("Все результаты начиная с 10:", above_10_results)
```
### Результат.
![ex2](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Practic/42.png)

## Выводы
sorted(): Эта функция используется для сортировки элементов в списке в порядке возрастания (по умолчанию) или в порядке, указанном пользователем. В данном коде sorted(results) сортирует элементы списка results в порядке возрастания. Аналогично, sorted(results) используется для получения худших результатов. Это позволяет найти три наилучших и три наихудших результатов.

List Comprehension ([result for result in results if result >= 10]): В данном случае, создается список above_10_results, содержащий только те элементы из списка results, которые больше или равны 10.


### 3) Преподаватель по математике придумал странную задачку. У вас есть три списка с элементами, каждый элемент которых – длина стороны треугольника, ваша задача найти площади двух треугольников, составленные из максимальных и минимальных элементов полученных списков. Результатом выполнения задачи будет: листинг кода, и вывод в консоль, в котором будут указаны два этих значения.
```python
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

```
### Результат.
![ex3](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Practic/43.png)

## Выводы
max(): Эта функция используется для нахождения максимального значения в итерируемом объекте. В коде max(one), max(two), и max(three) используются для нахождения максимальных значений в списках one, two и three. Результаты сохраняются в списке max_values.
min(): Эта функция используется для нахождения минимального значения в итерируемом объекте. В коде min(one), min(two), и min(three) используются для нахождения минимальных значений в списках one, two и three. Результаты сохраняются в списке min_values.
sort(): Этот метод используется для сортировки элементов списка в порядке возрастания. В коде max_values.sort() и min_values.sort() используются для сортировки списков max_values и min_values для последующего расчета площадей треугольников.
Функция calculate(sides): Эта функция определяет площадь треугольника на основе длин его сторон. Входной параметр sides является списком, содержащим длины трех сторон треугольника.


### 4) Никто не любит получать плохие оценки, поэтому Борис решил это исправить. Допустим, что все оценки студента за семестр хранятся в одном списке. Ваша задача удалить из этого списка все двойки, а все тройки заменить на четверки. 

```python
grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def update_grades(grades):
    updated_grades = []
    for grade in grades:
        if grade == 2:
            continue  # Пропускаем двойки
        elif grade == 3:
            updated_grades.append(4)  # Заменяем тройки на четверки
        else:
            updated_grades.append(grade)
    return updated_grades

updated_grades1 = update_grades(grades1)
updated_grades2 = update_grades(grades2)
updated_grades3 = update_grades(grades3)

print("Обновленный список оценок 1:", updated_grades1)
print("Обновленный список оценок 2:", updated_grades2)
print("Обновленный список оценок 3:", updated_grades3)
```
### Результат.
![ex4](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Practic/44.png)

## Выводы
Функция update_grades(grades): Эта пользовательская функция принимает список оценок grades в качестве входного параметра и возвращает обновленный список оценок updated_grades. Внутри функции происходит итерация по каждой оценке в списке grades. Если оценка равна 2, она пропускается (continue), если оценка равна 3, она заменяется на 4, в противном случае оценка остается без изменений. Это позволяет обновить список оценок в соответствии с указанными правилами.


### 5) 

```python

```
### Результат.
![ex5](https://github.com/kokac16/OZIVT_OKHLUPIN/blob/theme_5/pic/Practic/45.png)

## Выводы



## Общий вывод по теме
Базовые коллекции
Основные коллекции в Python включают в себя списки, множества и кортежи.
Коллекции - это структуры данных, которые позволяют хранить и манипулировать множеством значений.
Множества
Множество (set) - это коллекция уникальных элементов без порядка.
Множества полезны для операций над уникальными данными и проверки на вхождение элементов.
Списки
Список (list) - это упорядоченная коллекция элементов, которые могут быть разных типов.
Списки могут содержать повторяющиеся элементы.
Индексация списков:
Списки индексируются с помощью целых чисел, начиная с 0 для первого элемента.
Получение части списка:
Можно получить подсписок, указав начальный и конечный индексы.
Методы создания списков:
Список можно создать с помощью квадратных скобок [] или функции list().
Обращения к элементам:
Элементы списка доступны по индексам.
Индексы могут быть отрицательными для доступа с конца списка.
Разложение списков:
Разложение (slicing) позволяет получить часть списка.
Перебор списков через циклы:
Циклы, такие как for, позволяют перебирать элементы списка.
Сравнение списков:
Списки могут быть сравниваемы на равенство или неравенство.
Функции списков:
Списки поддерживают разнообразные функции, такие как len() (длина списка) и sum() (сумма элементов).
Методы списков:
Списки имеют множество методов для добавления, удаления, сортировки и манипулирования элементами.
Сортировка списков:
Списки могут быть отсортированы с помощью метода sort() или функции sorted().
Минимальное и максимальное значения в списке:
Функции min() и max() позволяют найти минимальное и максимальное значения в списке.
Копирование списков:
Копирование списка можно выполнить с помощью среза или метода copy().
Объединение (конкатенация) списков:
Списки можно объединять с помощью оператора + или метода extend().
Создание нового списка на основе двух или более списков:
Можно создать новый список, объединяя или комбинируя элементы из других списков.
Списки списков:
Списки могут содержать списки как свои элементы, что создает структуру списков списков для хранения данных.