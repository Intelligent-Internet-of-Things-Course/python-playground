"""
AudiCar: a child class that fixes the manufacturer to "Audi".

NOTE - bug fixed from the earlier version:
AudiCar.__init__ takes ONLY `model` (the manufacturer is always "Audi"),
so it must be built as AudiCar("Q3"), not AudiCar("Audi", "Q3").
The old main.py called it with two arguments and crashed with a TypeError -
exactly the kind of error described in python_best_practices.md 4.1.
"""

from car import Car

class AudiCar(Car):
    def __init__(self, model: str) -> None:
        super().__init__("Audi", model)
