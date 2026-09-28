"""
OOP hands-on - Step 08: custom exceptions.

A custom exception is just a class inheriting from Exception. It can carry
extra, domain-specific data (here: the battery level) alongside its message.
"""

class BatteryLowError(Exception):
    """Raised when the battery level is too low for operation."""

    def __init__(self, battery_level: int,
                 message: str = "Battery level is critically low!") -> None:
        self.battery_level = battery_level
        self.message = message
        super().__init__(f"{message} (Level: {battery_level}%)")

def operate_electric_car(battery_level: int) -> None:
    if battery_level < 20:
        raise BatteryLowError(battery_level)
    print(f"Car is operating normally (battery {battery_level}%).")
