"""
Networking hands-on (JSON) - the IoTDevice model.
Covers why a class beats a bare list for a device record.
"""

import json

class IoTDevice:
    def __init__(self, device_id: str, manufacturer: str, software_version: str,
                 latitude: float, longitude: float) -> None:
        self.device_id = device_id
        self.manufacturer = manufacturer
        self.software_version = software_version
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self) -> str:
        return (f"DeviceId: {self.device_id} - Manufacturer: {self.manufacturer} - "
                f"Software Version: {self.software_version} - "
                f"Lat/Lng: {self.latitude}/{self.longitude}")

    def to_json(self) -> str:
        # default=lambda o: o.__dict__ serialises any nested object by its attributes
        return json.dumps(self, default=lambda o: o.__dict__)

    # -> "IoTDevice" (in quotes): a forward reference - the class is not fully
    # defined yet on this line (same idea as oop/03 from_string).
    @classmethod
    def from_dict(cls, data: dict) -> "IoTDevice":
        """Rebuild an IoTDevice from a plain dict (e.g. json.loads output)."""
        return cls(**data)
