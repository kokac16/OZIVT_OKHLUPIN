from lab2 import Car

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity): 
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar ("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()    