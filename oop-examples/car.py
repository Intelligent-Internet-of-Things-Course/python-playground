import random


class Car:

    engine = "electric_engine"

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model

    # Instance method
    def description(self):
        return f"Manufacturer: {self.manufacturer} Model: {self.model}"

    # Replacement of the description method with the default __str__() method
    def __str__(self):
        return f"Manufacturer: {self.manufacturer} - Model: {self.model}"

    # Another instance method with a parameter
    def estimate_air_pollution(self, path_km_value):
        if self.engine == "electric_engine":
            return 0
        elif self.engine == "diesel_engine":
            return path_km_value*random.randint(20, 100)
        else:
            return -1
