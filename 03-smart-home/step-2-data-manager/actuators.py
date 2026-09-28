"""
Smart Home capstone - Step 1: Actuator base class + SmartLight.

Actuator mirrors Sensor but for "doing" instead of "measuring":
status + last_status_change_timestamp, and an informal-interface
invoke_action(action_type, payload).
"""

import time

from device import Device

class Actuator(Device):
    """Base class for all actuators."""

    def __init__(self, id: str, type: str, manufacturer: str) -> None:
        super().__init__(id, type, manufacturer)
        self.last_status_change_timestamp: float | None = None
        self.status: str | None = None  # e.g. "ON" / "OFF"

    # `payload: object` -> "any type at all" (same note as oop/02 __eq__);
    # each action decides what payload shape, if any, it expects.
    def invoke_action(self, action_type: str, payload: object) -> None:
        """Abstract method: concrete actuators must implement this."""
        raise NotImplementedError("Subclasses must implement this method.")

class SmartLight(Actuator):
    def __init__(self, id: str, initial_status: str = "OFF") -> None:
        super().__init__(id, "SmartLight", "GenericManufacturer")
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
