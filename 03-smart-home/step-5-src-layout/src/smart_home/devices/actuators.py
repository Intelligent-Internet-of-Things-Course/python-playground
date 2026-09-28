"""Actuator hierarchy (python_oop.md 4.6, 4.8) with type hints."""

import time

from smart_home.devices.base import Device


class Actuator(Device):
    def __init__(self, device_id: str, device_type: str, manufacturer: str) -> None:
        super().__init__(device_id, device_type, manufacturer)
        self.last_status_change_timestamp: float | None = None
        self.status: str | None = None

    def invoke_action(self, action_type: str, payload: object = None) -> None:
        raise NotImplementedError("Subclasses must implement this method.")


class SmartLight(Actuator):
    def __init__(self, device_id: str, initial_status: str = "OFF") -> None:
        super().__init__(device_id, "SmartLight", "GenericManufacturer")
        self.status = initial_status
        self.last_status_change_timestamp = time.time() * 1000

    def invoke_action(self, action_type: str, payload: object = None) -> None:
        if action_type == "turn_on":
            self.status = "ON"
        elif action_type == "turn_off":
            self.status = "OFF"
        else:
            raise ValueError(f"Unknown action type: {action_type}")
        self.last_status_change_timestamp = time.time() * 1000
