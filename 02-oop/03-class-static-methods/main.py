"""
Run:  python3 main.py

Walk-through (python_oop.md 2.5):
  1. total_cars is shared: every Car(...) call bumps the same counter;
  2. Car.from_string("A-B") is a second way to build a Car;
  3. is_valid_manufacturer() touches neither the class nor an instance;
  4. attribute_shadowing.py - reading an attribute falls back to the class,
     but assigning it always creates a separate instance attribute;
  5. class_attribute_pitfalls.py - the two bugs that fall out of (4) in
     practice (a shared mutable list, an accidentally-shadowed counter),
     plus a reminder that UPPER_CASE constants are only a convention.
"""

import attribute_shadowing
import class_attribute_pitfalls
from car import Car


def main() -> None:
    car_1 = Car("Toyota", "Corolla")
    car_2 = Car("Honda", "Civic")
    car_3 = Car.from_string("Ford-Focus")     # alternative constructor

    print("car_3 built from string ->", car_3)

    # class attribute read through the class (preferred) and an instance
    print("Car.wheels      ->", Car.wheels)
    print("car_1.wheels    ->", car_1.wheels)

    # 2.5.2 - the class method reports the shared state correctly,
    # even though it was never told about car_1 / car_2 / car_3 individually
    print("get_total_cars() ->", Car.get_total_cars())    # 3

    # 2.5.3 - static utility
    print("is_valid_manufacturer('Toyota') ->", Car.is_valid_manufacturer("Toyota"))
    print("is_valid_manufacturer('')       ->", Car.is_valid_manufacturer(""))

    print()
    print("=== attribute_shadowing.py: class vs instance attributes ===")
    attribute_shadowing.main()

    print()
    print("=== class_attribute_pitfalls.py: two bugs that follow from it ===")
    class_attribute_pitfalls.main()


if __name__ == "__main__":
    main()
