"""
OOP hands-on - Step 03 (extra): class attributes vs instance attributes -
what actually changes.

Reading `instance.attribute` first looks for an attribute on the INSTANCE,
and only falls back to the CLASS attribute if the instance has none.
Assigning `instance.attribute = value` never touches the class attribute at
all - it always creates a new, separate attribute on that one instance,
permanently shadowing the class attribute for it from then on.
"""


class Car:
    wheels = 4  # class attribute: shared, until an instance shadows it

    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model


def main() -> None:
    car_1 = Car("Toyota", "Corolla")
    car_2 = Car("Honda", "Civic")

    # neither instance has its own `wheels` yet -> both fall back to Car.wheels
    print("start           ->", car_1.wheels, car_2.wheels)          # 4 4

    # (1) reassigning the CLASS attribute: both still fall back, both see it
    Car.wheels = 6
    print("Car.wheels = 6  ->", car_1.wheels, car_2.wheels)          # 6 6

    # (2) assigning directly on ONE instance creates a NEW instance attribute -
    # it does NOT touch Car.wheels
    car_1.wheels = 3
    print("car_1.wheels = 3 ->", car_1.wheels, car_2.wheels)         # 3 6

    # (3) reassigning the class attribute again: car_1 no longer notices,
    # because it now has its own instance attribute shadowing it
    Car.wheels = 8
    print("Car.wheels = 8  ->", car_1.wheels, car_2.wheels)          # 3 8


if __name__ == "__main__":
    main()
