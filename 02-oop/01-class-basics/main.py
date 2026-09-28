"""
Run:  python3 main.py

Walk-through (python_oop.md 2.2 - 2.3):
  1. two instances of the same class are two distinct objects;
  2. default equality compares identity (memory address), not content;
  3. attributes are read and changed with dot notation;
  4. a required argument left out raises TypeError - CarWithDefaults shows
     the fix (2.3.3).
"""

from car import Car, CarWithDefaults


def main() -> None:
    # 2.2.3 - multiple instances of the same class
    car_1 = Car("Toyota", "Corolla")
    car_2 = Car("Honda", "Civic")

    print(car_1)                 # <car.Car object at 0x...> - no __str__ yet (see step 02)
    print(car_2)
    print("car_1 == car_2 ->", car_1 == car_2)   # False: compared by identity

    # 2.3.4 - access instance attributes
    print(f"Car 1 -> Manufacturer: {car_1.manufacturer} Model: {car_1.model}")
    print(f"Car 2 -> Manufacturer: {car_2.manufacturer} Model: {car_2.model}")

    # 2.3.5 - change instance attributes at runtime
    car_1.model = "Yaris"
    print(f"Car 1 after update -> Model: {car_1.model}")

    # each instance keeps its own state: car_2 is untouched
    print(f"Car 2 is unchanged -> Model: {car_2.model}")

    # 2.3.3 - a required argument left out raises TypeError
    try:
        Car()
    except TypeError as e:
        print("Car() fails ->", e)

    # ... unless the parameters have default values
    car_3 = CarWithDefaults()
    print(f"CarWithDefaults() -> Manufacturer: {car_3.manufacturer} Model: {car_3.model}")


if __name__ == "__main__":
    main()
