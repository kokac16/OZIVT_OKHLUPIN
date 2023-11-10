from lab2 import Car
class Car:
    def __init__(self, make, model):
        self._make = make 

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car = Car ("Lada", "Kalina")
print(my_car. _make) 

my_car.drive()