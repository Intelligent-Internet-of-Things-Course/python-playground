"""
Run:  python3 main.py

Walk-through (python_oop.md 2.6), in the lecture's own order:
  1. access_modifiers.py - public / protected / private are only a naming
     CONVENTION; a "private" attribute is still reachable via name mangling;
  2. getters_setters.py - get_model()/set_model() validate the new value,
     but change how callers use the attribute;
  3. car.py - @property removes exactly that drawback: reading/writing
     car.model looks like plain attribute access, but a method (with
     validation) runs behind it, including inside __init__;
  4. `del car.model` goes through the .deleter.
"""

import access_modifiers
import getters_setters
from car import Car


def main() -> None:
    print("=== access_modifiers.py (2.6.1) ===")
    access_modifiers.main()

    print()
    print("=== getters_setters.py (2.6.2) ===")
    getters_setters.main()

    print()
    print("=== car.py: @property / .setter / .deleter (2.6.3) ===")
    car = Car("Toyota", "Corolla", "AB123CD")
    print("start ->", car)

    # write goes through @model.setter
    car.model = "Yaris"
    print("after car.model = 'Yaris' ->", car.model)

    # setter validation
    try:
        car.model = ""
    except ValueError as e:
        print("rejected:", e)

    try:
        car.license_plate = "X"
    except ValueError as e:
        print("rejected:", e)

    # even construction is validated: this Car is never created
    try:
        Car("Fiat", "Panda", "TOO-LONG-PLATE")
    except ValueError as e:
        print("rejected at construction:", e)

    # deleter
    del car.model
    print("model deleted; hasattr(car, '_model') ->", hasattr(car, "_model"))


if __name__ == "__main__":
    main()
