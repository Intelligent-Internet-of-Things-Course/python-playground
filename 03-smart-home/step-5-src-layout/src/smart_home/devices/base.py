"""The Device base class (python_oop.md 4.4), now with type hints."""


class Device:
    """Base class for all devices: shared identifying data, no behaviour."""

    def __init__(self, device_id: str, device_type: str, manufacturer: str) -> None:
        # unlike the lecture's `id`/`type`, these names avoid shadowing built-ins
        self.id = device_id
        self.type = device_type
        self.manufacturer = manufacturer

    def __str__(self) -> str:
        return f"{self.type}({self.id}) by {self.manufacturer}"
