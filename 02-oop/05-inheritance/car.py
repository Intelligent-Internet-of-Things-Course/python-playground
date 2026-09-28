"""
OOP hands-on - Step 05: inheritance.
Covers parent class, super(), method overriding.

NOTE - alignment with the lecture:
The earlier version of this file made estimate_air_pollution() branch on an
`engine` class attribute. The lecture (2.7.1) instead uses a GENERIC Car that
cannot know its engine, so it returns the sentinel value -1 ("not available"),
and lets concrete subclasses override it with a real computation. This file
now follows the lecture; the engine-based variant is discussed in the main
README.
"""

class Car:
    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model

    def __str__(self) -> str:
        return f"Manufacturer: {self.manufacturer} Model: {self.model}"

    def estimate_air_pollution(self, path_km_value: float) -> float:
        # A generic Car has no information about its engine / fuel type,
        # so it cannot produce a real estimate: -1 signals "not available".
        # Concrete subclasses override this with a real computation.
        return -1
