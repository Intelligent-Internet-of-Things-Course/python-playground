"""
Smart Home capstone - Step 4b: Factory pattern.

Problem: create objects without the caller depending on their concrete
classes. Solution: centralise creation in a DeviceFactory that returns the
right instance from a type string.

SmartLock below is a brand-new actuator, added by writing one class and one
`elif` branch - none of the existing branches change.
"""

import time

from device import Device
from actuators import Actuator, SmartLight
from sensors import TemperatureSensor, HumiditySensor

class SmartLock(Actuator):
    def __init__(self, id: str, initial_status: str = "LOCKED") -> None:
        super().__init__(id, "SmartLock", "GenericManufacturer")
        self.status = initial_status
        self.last_status_change_timestamp = time.time() * 1000

    def invoke_action(self, action_type: str, payload: object = None) -> None:
        if action_type == "lock":
            self.status = "LOCKED"
        elif action_type == "unlock":
            self.status = "UNLOCKED"
        else:
            raise ValueError(f"Unknown action type: {action_type}")
        self.last_status_change_timestamp = time.time() * 1000

class DeviceFactory:
    # -> Device: the factory promises "some Device subclass", without the
    # caller needing to know which concrete one (references 4.5 + a custom
    # class as the type).
    @staticmethod
    def create_device(device_type: str, id: str) -> Device:
        if device_type == "temperature":
            return TemperatureSensor(id)
        elif device_type == "humidity":
            return HumiditySensor(id)
        elif device_type == "light":
            return SmartLight(id)
        elif device_type == "lock":                 # the only new branch
            return SmartLock(id)
        else:
            raise ValueError(f"Unknown device type: {device_type}")
