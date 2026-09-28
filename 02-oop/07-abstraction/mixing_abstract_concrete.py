"""
OOP hands-on - Step 07c: mixing abstract and concrete methods.

Reference: python_oop.md 2.9 ("Mixing Abstract and Concrete Methods").

formal.py used @abstractmethod on EVERY method, making Vehicle behave like a
pure interface. An ABC is not limited to that: it can mix @abstractmethod
methods (every subclass MUST override them) with ordinary, fully-implemented
methods (inherited AS-IS, with no need to override them at all) - and even
shared state (attributes) set up in __init__. A single class can therefore
act as a pure interface, a partial "abstract class", or anything in between,
depending only on which of its methods carry @abstractmethod.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self) -> None:
        self.total_trips = 0

    # Concrete method: a normal def, no @abstractmethod - implemented once
    # here, and inherited unchanged by every subclass.
    def register_trip(self) -> str:
        self.total_trips += 1
        return f"Trip registered. Total trips: {self.total_trips}"

    # Abstract method: every concrete subclass MUST still override this.
    @abstractmethod
    def start(self) -> str:
        ...


class Car(Vehicle):
    def start(self) -> str:
        return "Car engine starting..."


def main() -> None:
    car = Car()
    print(car.start())            # Car's own implementation
    print(car.register_trip())    # inherited from Vehicle, unmodified
    print(car.register_trip())


if __name__ == "__main__":
    main()
