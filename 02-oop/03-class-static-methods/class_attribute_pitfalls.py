"""
OOP hands-on - Step 03 (extra): two common class-attribute bugs.

  1. a MUTABLE class attribute (a list/dict/set) is one single object shared
     by every instance - mutating it through one instance leaks into all of
     them, even though nothing was ever assigned to that instance;
  2. `self.counter += 1` on what was meant to be a shared class attribute
     silently creates a new, separate INSTANCE attribute instead of
     updating the shared one - the read falls back to the class, but the
     write always lands on the instance.

Each pitfall is shown broken, then fixed, side by side.
"""


# --- pitfall 1: mutable class attribute --------------------------------

class CarMutableBug:
    passengers: list[str] = []  # DANGER: one single list, shared by every instance

    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model


class CarMutableFixed:
    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.passengers: list[str] = []  # instance attribute: a fresh list per car


def demo_mutable_class_attribute() -> None:
    print("--- pitfall 1: mutable class attribute (list/dict/set) ---")

    car_1 = CarMutableBug("Toyota", "Corolla")
    car_2 = CarMutableBug("Honda", "Civic")
    car_1.passengers.append("Alice")           # a MUTATION, not an assignment
    print("buggy -> car_1.passengers:", car_1.passengers)
    print("buggy -> car_2.passengers:", car_2.passengers, "<- BUG: car_2 never touched it")

    car_3 = CarMutableFixed("Toyota", "Corolla")
    car_4 = CarMutableFixed("Honda", "Civic")
    car_3.passengers.append("Alice")
    print("fixed -> car_3.passengers:", car_3.passengers)
    print("fixed -> car_4.passengers:", car_4.passengers, "<- correct: untouched")


# --- pitfall 2: accidentally shadowing a shared counter -----------------

class CarShadowBug:
    total_cars = 0

    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.total_cars += 1  # BUG: reads the class attribute, writes an INSTANCE one


class CarShadowFixed:
    total_cars = 0

    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model
        CarShadowFixed.total_cars += 1  # correct: updates the shared counter explicitly


def demo_shadowed_counter() -> None:
    print("--- pitfall 2: accidentally shadowing a shared counter ---")

    CarShadowBug("Toyota", "Corolla")
    car = CarShadowBug("Honda", "Civic")
    print("buggy -> CarShadowBug.total_cars:", CarShadowBug.total_cars, "<- never actually incremented!")
    print("buggy -> car.total_cars:", car.total_cars, "<- car's own, independent instance attribute")

    CarShadowFixed("Toyota", "Corolla")
    CarShadowFixed("Honda", "Civic")
    print("fixed -> CarShadowFixed.total_cars:", CarShadowFixed.total_cars, "<- correctly shared")


# --- bonus: Python has no real constants ---------------------------------

class Car:
    MAX_PASSENGERS = 5  # UPPER_CASE: a naming CONVENTION signalling "do not change"


def demo_no_real_constants() -> None:
    print("--- bonus: UPPER_CASE is only a convention, not enforcement ---")
    print("before ->", Car.MAX_PASSENGERS)
    Car.MAX_PASSENGERS = 10  # nothing stops this - Python has no `const` / `final`
    print("after  ->", Car.MAX_PASSENGERS, "<- silently changed, no error, no warning")


def main() -> None:
    demo_mutable_class_attribute()
    print()
    demo_shadowed_counter()
    print()
    demo_no_real_constants()


if __name__ == "__main__":
    main()
