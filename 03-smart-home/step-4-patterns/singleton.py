"""
Smart Home capstone - Step 4a: Singleton pattern.

Problem: guarantee that only ONE instance of a class exists, reachable from
anywhere. Solution: control creation in __new__ (python_oop.md 2.4.4) and
return the same instance every time.

Here: a Smart Home should never end up with two independent DataManagers,
each with its own inconsistent view of the devices.
"""

class DataManager:
    """DataManager, restricted to a single shared instance."""

    _instance = None

    # __new__ is left un-annotated on purpose: typing it correctly is an
    # advanced topic, beyond references python_best_practices.md 4.5
    # (same choice as oop/02-methods-dunder/car.py).
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.devices = []
        return cls._instance
