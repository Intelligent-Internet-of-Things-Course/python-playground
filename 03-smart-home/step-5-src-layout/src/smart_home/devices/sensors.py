"""Sensor hierarchy (python_oop.md 4.5, 4.7) with type hints."""

import random
import time

from smart_home.devices.base import Device


class Sensor(Device):
    def __init__(self, device_id: str, device_type: str, manufacturer: str) -> None:
        super().__init__(device_id, device_type, manufacturer)
        self.last_measurement_timestamp: float | None = None
        self.last_measurement_value: float | None = None

    def update_value(self) -> None:
        raise NotImplementedError("Subclasses must implement this method.")


class TemperatureSensor(Sensor):
    def __init__(self, device_id: str, initial_temperature_value: float = 25.0) -> None:
        super().__init__(device_id, "TemperatureSensor", "GenericManufacturer")
        self.last_measurement_value = initial_temperature_value
        self.last_measurement_timestamp = time.time() * 1000

    def update_value(self) -> None:
        self.last_measurement_value = random.uniform(15.0, 30.0)
        self.last_measurement_timestamp = time.time() * 1000


class HumiditySensor(Sensor):
    def __init__(self, device_id: str, initial_humidity_value: float = 50.0) -> None:
        super().__init__(device_id, "HumiditySensor", "GenericManufacturer")
        self.last_measurement_value = initial_humidity_value
        self.last_measurement_timestamp = time.time() * 1000

    def update_value(self) -> None:
        self.last_measurement_value = random.uniform(30.0, 90.0)
        self.last_measurement_timestamp = time.time() * 1000
