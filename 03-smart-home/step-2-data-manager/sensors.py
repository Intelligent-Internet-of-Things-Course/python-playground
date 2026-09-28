"""
Smart Home capstone - Step 1: Sensor base class + concrete sensors.

Sensor inherits id/type/manufacturer from Device, adds the measurement
attributes, and declares update_value() as an INFORMAL interface
(raises NotImplementedError - see python_oop.md 2.9.1). Each concrete sensor
provides its own update_value().
"""

import random
import time

from device import Device

class Sensor(Device):
    """Base class for all sensors."""

    def __init__(self, id: str, type: str, manufacturer: str) -> None:
        super().__init__(id, type, manufacturer)
        # `float | None`: starts empty, holds a reading later (references 4.5)
        self.last_measurement_timestamp: float | None = None
        self.last_measurement_value: float | None = None

    def update_value(self) -> None:
        """Abstract method: concrete sensors must implement this."""
        raise NotImplementedError("Subclasses must implement this method.")

class TemperatureSensor(Sensor):
    def __init__(self, id: str, initial_temperature_value: float = 25.0) -> None:
        super().__init__(id, "TemperatureSensor", "GenericManufacturer")
        self.last_measurement_value = initial_temperature_value
        self.last_measurement_timestamp = time.time() * 1000

    def update_value(self) -> None:
        self.last_measurement_value = random.uniform(15.0, 30.0)
        self.last_measurement_timestamp = time.time() * 1000

class HumiditySensor(Sensor):
    def __init__(self, id: str, initial_humidity_value: float = 50.0) -> None:
        super().__init__(id, "HumiditySensor", "GenericManufacturer")
        self.last_measurement_value = initial_humidity_value
        self.last_measurement_timestamp = time.time() * 1000

    def update_value(self) -> None:
        self.last_measurement_value = random.uniform(30.0, 90.0)
        self.last_measurement_timestamp = time.time() * 1000
