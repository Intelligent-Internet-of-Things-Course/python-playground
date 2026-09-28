"""
Networking hands-on (JSON) - the ServiceMessage envelope.

TEACHING POINT - nested deserialization:
`ServiceMessage(**json.loads(text))` reconstructs the envelope but leaves
`iot_device` as a plain dict, NOT an IoTDevice. json.loads() has no idea
which class a nested object should become. from_json() below fixes that by
rebuilding the nested IoTDevice explicitly.
"""

import json

from iot_device import IoTDevice


class ServiceMessage:
    # iot_device: "IoTDevice | dict" -> beyond references 4.5. `A | B` means
    # "either type"; it is a plain dict right after json.loads(), and a real
    # IoTDevice once from_json() has rebuilt it. Quotes: forward reference.
    def __init__(self, action_command: str, iot_device: "IoTDevice | dict") -> None:
        self.action_command = action_command
        self.iot_device = iot_device

    def __str__(self) -> str:
        return f"Action Command: {self.action_command} - Target IoT Device: {self.iot_device}"

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def from_json(cls, text: str) -> "ServiceMessage":
        """Parse JSON text AND rebuild the nested IoTDevice as a real object."""
        data = json.loads(text)
        device = data["iot_device"]
        if isinstance(device, dict):
            device = IoTDevice.from_dict(device)
        return cls(data["action_command"], device)
