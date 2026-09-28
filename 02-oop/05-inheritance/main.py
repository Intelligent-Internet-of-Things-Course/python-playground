"""
Run:  python3 main.py

Walk-through (python_oop.md 2.7):
  1. ElectricCar inherits __str__ / estimate_air_pollution from Car, then
     overrides both;
  2. the same call (print(x), x.estimate_air_pollution(100)) gives a
     different result depending on the actual class -> polymorphism;
  3. type() / isinstance() inspect the class hierarchy;
  4. __mro__ shows the exact lookup order Python uses (single inheritance
     here; inheritance_variants.py covers multilevel, multiple, and a real
     MRO conflict).
"""

import inheritance_variants
from car import Car
from audi import AudiCar
from electric_car import ElectricCar


def main() -> None:
    car = Car("Toyota", "Corolla")
    audi = AudiCar("Q3")                       # fixed: one argument only
    ecar = ElectricCar("Tesla", "Model-Y", 60)

    # 2.7.2 - same interface, different behaviour
    print(car)                                 # Manufacturer: Toyota Model: Corolla
    print("  pollution:", car.estimate_air_pollution(100))    # -1 (not available)

    print(ecar)                                # ... - Kwh: 60
    print("  pollution:", ecar.estimate_air_pollution(100))   # 0 (overridden)

    print(audi)                                # Manufacturer: Audi Model: Q3

    # ElectricCar-only method
    ecar.measure_battery_level()
    print("  battery level:", ecar.battery_level)

    # 2.7.1 - inspecting types
    print("type(audi)          ->", type(audi).__name__)
    print("isinstance(audi, Car)->", isinstance(audi, Car))

    # 2.7.4 - every class ultimately derives from the built-in `object`
    print("issubclass(Car, object)               ->", issubclass(Car, object))
    print("isinstance(Car('Audi', 'A4'), object) ->", isinstance(Car("Audi", "A4"), object))

    # 2.7.4 - Method Resolution Order (single inheritance: a linear chain)
    print("ElectricCar MRO ->", [c.__name__ for c in ElectricCar.__mro__])

    print()
    print("=== inheritance_variants.py: multilevel, multiple, MRO conflicts ===")
    inheritance_variants.main()


if __name__ == "__main__":
    main()
