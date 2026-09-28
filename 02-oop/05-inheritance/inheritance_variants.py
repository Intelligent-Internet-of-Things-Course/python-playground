"""
OOP hands-on - Step 05 (extra): multilevel/multiple inheritance and MRO.

Reference: python_oop.md 2.7.3, 2.7.4.

car.py / electric_car.py / audi.py only show SINGLE inheritance (one parent).
This file covers the other two shapes, plus what happens when two parents
define the SAME method name.
"""


# --- multilevel inheritance: A -> B -> C, one parent per level -----------

class Vehicle:
    pass


class Car(Vehicle):
    pass


class ElectricCar(Car):
    pass


# --- multiple inheritance: one class, two parents at once ----------------

class Chargeable:
    pass


class Connected:
    pass


class SmartElectricCar(Chargeable, Connected):
    pass


# --- MRO: which parent wins when two of them define the same method? -----

class Base1:
    def greet(self) -> str:
        return "hi!"


class Base2:
    def greet(self) -> str:
        return "hello!"


class MultiDerived(Base1, Base2):
    pass


# "Let's See How It Works" (2.7.4): same shape, a real name conflict

class A:
    def who(self) -> str:
        return "A"


class B:
    def who(self) -> str:
        return "B"


class C(A, B):
    pass


def main() -> None:
    print("--- multilevel inheritance (2.7.3) ---")
    ecar = ElectricCar()
    print("isinstance(ecar, Car)     ->", isinstance(ecar, Car))
    print("isinstance(ecar, Vehicle) ->", isinstance(ecar, Vehicle))

    print("--- multiple inheritance (2.7.3) ---")
    smart_car = SmartElectricCar()
    print("isinstance(smart_car, Chargeable) ->", isinstance(smart_car, Chargeable))
    print("isinstance(smart_car, Connected)  ->", isinstance(smart_car, Connected))

    print("--- MRO (2.7.4) ---")
    m = MultiDerived()
    print("m.greet() ->", m.greet(), "<- Base1 is searched before Base2")
    print("MultiDerived.__mro__ ->", [c.__name__ for c in MultiDerived.__mro__])

    print("--- MRO, a real conflict (2.7.4, Let's See How It Works) ---")
    print("C().who() ->", C().who())
    print("C.mro()   ->", [c.__name__ for c in C.mro()])


if __name__ == "__main__":
    main()
