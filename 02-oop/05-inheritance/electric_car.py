"""
ElectricCar: a child class of Car.
"""

import random

from car import Car

class ElectricCar(Car):
    """ElectricCar inherits from Car and adds electric-specific attributes."""

    def __init__(self, manufacturer: str, model: str, kwh: float) -> None:
        # run the parent initialisation instead of duplicating it
        super().__init__(manufacturer, model)
        self.kwh = kwh
        self.battery_level = 100  # percentage

    # OVERRIDE: reuse the parent text via super(), then add to it
    def __str__(self) -> str:
        return f"{super().__str__()} - Kwh: {self.kwh}"

    # OVERRIDE: replace the -1 sentinel with a real, meaningful value
    def estimate_air_pollution(self, path_km_value: float) -> float:
        return 0  # electric cars produce zero direct air pollution

    # NEW method: Car has nothing like this
    def measure_battery_level(self) -> int:
        self.battery_level = random.randint(10, 100)
        return self.battery_level
