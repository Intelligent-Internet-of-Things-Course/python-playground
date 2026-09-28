"""
OOP hands-on - Step 06b: polymorphism via method overriding.

Reference: python_oop.md 2.8.4.

Overriding a method in a subclass (Section 2.7.2) is itself a form of
polymorphism: the SAME method call, through the SAME interface, produces a
DIFFERENT result depending on the actual class of the object it is called
on. Car/ElectricCar are reproduced here (matching 05-inheritance) so this
step stays self-contained.

Unlike 2.8.3 (unrelated classes, no enforced contract), ElectricCar genuinely
IS a Car (isinstance(ecar, Car) is True), so a new subclass can be added
later - e.g. a HydrogenCar(Car) - WITHOUT ever touching the loop below, as
long as it overrides estimate_air_pollution() too. This is the Open/Closed
Principle: the loop stays closed for modification, the hierarchy stays open
for extension. Python resolves, at run time, WHICH implementation actually
runs - this is called dynamic dispatch.
"""


class Car:
    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model

    def __str__(self) -> str:
        return f"Manufacturer: {self.manufacturer} Model: {self.model}"

    def estimate_air_pollution(self, path_km_value: float) -> float:
        # A generic Car has no information about its engine/fuel type.
        return -1


class ElectricCar(Car):
    def __init__(self, manufacturer: str, model: str, kwh: float) -> None:
        super().__init__(manufacturer, model)
        self.kwh = kwh

    # Overrides Car.estimate_air_pollution() with a real, meaningful value.
    def estimate_air_pollution(self, path_km_value: float) -> float:
        return 0


def main() -> None:
    car = Car("Toyota", "Corolla")
    ecar = ElectricCar("Tesla", "Model 3", 75)

    fleet = [car, ecar]
    for vehicle in fleet:
        # The exact same call, vehicle.estimate_air_pollution(100), every time...
        print(f"{vehicle.manufacturer} {vehicle.model}: {vehicle.estimate_air_pollution(100)}")

    print("isinstance(ecar, Car) ->", isinstance(ecar, Car))


if __name__ == "__main__":
    main()
