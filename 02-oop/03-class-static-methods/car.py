"""
OOP hands-on - Step 03: class attributes, class methods, static methods.
Covers shared class attributes, @classmethod with `cls`, @staticmethod,
and the "alternative constructor" pattern with from_string().
"""

class Car:
    # 2.5.1 - CLASS attributes: shared by every instance
    wheels = 4
    total_cars = 0

    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model
        # increment the SHARED counter every time a Car is built
        Car.total_cars += 1

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model}"

    # 2.5.2 - class method: receives the class (`cls`), not an instance
    @classmethod
    def get_total_cars(cls) -> int:
        return cls.total_cars

    # 2.5.2 - alternative constructor: parse a string, then call cls(...).
    # Return type "Car" (in quotes) -> beyond references 4.5, two things at once:
    #   * a class name is itself a valid type annotation, like `int` or `str`;
    #   * the quotes make it a "forward reference": on this line the class
    #     `Car` is not fully defined yet, so its name is given as a string.
    @classmethod
    def from_string(cls, car_string: str) -> "Car":
        # e.g. "Toyota-Corolla" -> Car("Toyota", "Corolla")
        manufacturer, model = car_string.split("-")
        return cls(manufacturer, model)

    # 2.5.3 - static method: no `self`, no `cls`; just grouped inside the class.
    # `name: object` -> "any type at all" (same note as oop/02 __eq__).
    @staticmethod
    def is_valid_manufacturer(name: object) -> bool:
        return isinstance(name, str) and len(name) > 0
