from car import Car


class AudiCar(Car):

    def __init__(self, model):
        super().__init__("Audi", model)
