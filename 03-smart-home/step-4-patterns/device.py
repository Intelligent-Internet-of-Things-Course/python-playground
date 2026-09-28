"""
Smart Home capstone - Step 1: the Device base class.

Device holds only the data every device shares (id, type, manufacturer) and
no behaviour. Sensor and Actuator specialise it.

Note: `id` and `type` shadow Python built-ins; the name choice follows the
lecture verbatim so the cross-reference stays exact.
"""

class Device:
    """Base class for all devices in the Smart Home IoT system."""

    def __init__(self, id: str, type: str, manufacturer: str) -> None:
        self.id = id
        self.type = type
        self.manufacturer = manufacturer
