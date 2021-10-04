from car import Car
import random


class ElectricCar(Car):

    engine = "electric_engine"

    # Another instance method with an additional parameter
    def __init__(self, manufacturer, model, kwh):
        super().__init__(manufacturer, model)
        self.kwh = kwh
        self.battery_level = 100

    def __str__(self):
        return f"{super().__str__()} - Kwh: {self.kwh}"

    def estimate_air_pollution(self, path_km_value):
        return 0

    def measure_battery_level(self):
        self.battery_level = random.randint(10, 100)
        return self.battery_level
