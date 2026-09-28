"""
Run:  python3 main.py

Walk-through (python_oop.md 2.4):
  1. __new__ runs before __init__ (see the printed order);
  2. print(car) now calls __str__ instead of showing a memory address;
  3. __eq__ makes two cars with the same data compare as equal;
  4. `del` triggers __del__.
"""

from car import Car


def main() -> None:
    print("Creating car_1:")
    car_1 = Car("Toyota", "Corolla")

    print("Creating car_2 (same data as car_1):")
    car_2 = Car("Toyota", "Corolla")

    # 2.4.1 / 2.4.2
    print("description():", car_1.description())
    print("print(car_1) :", car_1)          # __str__

    # 2.4.3 - content-based equality
    print("car_1 == car_2 ->", car_1 == car_2)      # True (same manufacturer/model)
    print("car_1 is car_2 ->", car_1 is car_2)      # False (still two objects)

    # 2.4.5 - explicit destruction
    print("Deleting car_1:")
    del car_1


if __name__ == "__main__":
    main()
