"""
OOP hands-on - Step 07b: FORMAL abstraction with abc.

A class inheriting from ABC with @abstractmethod methods cannot be
instantiated until EVERY abstract method is overridden - the check happens
at instantiation time, not only when the method is eventually called.
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self) -> str:
        ...

    @abstractmethod
    def stop(self) -> str:
        ...

class Car(Vehicle):
    def start(self) -> str:
        return "Car engine starting..."

    def stop(self) -> str:
        return "Car engine stopping..."

class Motorcycle(Vehicle):
    def start(self) -> str:
        return "Motorcycle engine starting..."
    # stop() is deliberately NOT implemented
