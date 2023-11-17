class Tomato:
    # 1) Создайте класс Tomato
    # 2) Создайте статическое свойство states, которое будет содержать все
    # стадии созревания помидора
    states = ['отсутствует', 'цветение', 'зеленый', 'красный']

    # 3) Создайте метод __init__(), внутри которого будут определены два
    # динамических свойства: _index (передается параметром) и _state (принимает первое значение из словаря states).
    # После написания этого блока кода в комментарии к нему укажите какими являются
    # эти два свойства
    def __init__(self, index):
        self._index = index  # _index - динамическое свойство, передается параметром
        self._state = self.states[-1]  # _state - динамическое свойство, принимает первое значение из списка states

    # 4) Создайте метод grow(), который будет переводить томат на следующую стадию созревания
    def grow(self):
        current_state_index = self.states.index(self._state)
        if current_state_index < len(self.states) - 1:
            self._state = self.states[current_state_index + 1]

    # 5) Создайте метод is_ripe(), который будет проверять, что томат созрел
    def is_ripe(self):
        return self._state == self.states[-1]


class TomatoBush:
    # 1) Создайте класс TomatoBush
    def __init__(self, num_tomatoes):
        # 2) Определите метод __init__(), который будет принимать в качестве
        # параметра количество томатов и на его основе будет создавать
        # список объектов класса Tomato. Данный список будет храниться
        # внутри динамического свойства tomatoes
        self.tomatoes = [Tomato(index=i) for i in range(1, num_tomatoes + 1)]

    # 3) Создайте метод grow_all(), который будет переводить все объекты
    # из списка томатов на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # 4) Создайте метод all_are_ripe(), который будет возвращать True, если
    # все томаты из списка стали спелыми.
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # 5) Создайте метод give_away_all(), который будет чистить список
    # томатов после сбора урожая
    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    # 1) Создайте класс Gardener
    # 2) Создайте метод __init__(), внутри которого будут определены два
    # динамических свойства: name (передается параметром, является
    # публичным) и _plant (принимает объект класса TomatoBush).
    # После написания этого блока кода в комментарии к нему укажите какими
    # являются эти два свойства
    def __init__(self, name, plant):
        self.name = name  # name - динамическое свойство, передается параметром, публичное
        self._plant = plant  # _plant - динамическое свойство, принимает объект класса TomatoBush

    # 3) Создайте метод work(), который заставляет садовника работать, что
    # позволяет растению становиться более зрелым
    def work(self):
        self._plant.grow_all()

    # 4) Создайте метод harvest(), который проверяет, все ли плоды созрели.
    # Если все, то садовник собирает урожай. Если нет, то метод печатает предупреждение
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай!")
            self._plant.give_away_all()
        else:
            print("Плоды еще не все созрели. Подождите немного.")

    # 5) Создайте статический метод knowledge_base(), который выведет в
    # консоль справку по садоводству
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: чето инфа про помидоры")


# Тесты:
# 1) Вызовите справку по садоводству
Gardener.knowledge_base()

# 2) Создайте объекты классов TomatoBush и Gardener
bush = TomatoBush(num_tomatoes=10)
gardener = Gardener(name="Иван", plant = bush)

# 3) Используя объект класса Gardener, поухаживайте за кустом с помидорами
gardener.work()

# 4) Попробуйте собрать урожай, когда томаты еще не дозрели.
# Продолжайте ухаживать 6за ними
gardener.harvest()
gardener.work()

# 5) Соберите урожай
gardener.harvest()
