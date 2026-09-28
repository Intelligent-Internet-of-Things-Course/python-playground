"""
Smart Home capstone - Step 2: the DataManager.

DELEGATION: the SmartHome (step 3) should not manage device storage itself.
That responsibility is handed to a dedicated DataManager, so the storage
strategy (in-memory dict/list today, a database tomorrow) can change here
without touching the SmartHome. This is the first, informal design pattern
of the course (python_oop.md 7.3).
"""

from device import Device
from sensors import Sensor
from actuators import Actuator

class DataManager:
    """Owns device storage and the latest known data for each device."""

    def __init__(self) -> None:
        # beyond references 4.5:
        #   list[Device]   -> list[...] (4.5) also works with your own classes
        #   dict[str, dict] -> same list[float] idea (4.5), applied to a dict
        self.devices: list[Device] = []
        self.sensor_data: dict[str, dict] = {}

    def add_device(self, device: Device) -> None:
        self.devices.append(device)
        if isinstance(device, Sensor):
            self.sensor_data[device.id] = {
                "last_measurement_timestamp": device.last_measurement_timestamp,
                "last_measurement_value": device.last_measurement_value,
            }
        elif isinstance(device, Actuator):
            self.sensor_data[device.id] = {
                "last_status_change_timestamp": device.last_status_change_timestamp,
                "status": device.status,
            }

    def remove_device(self, device_id: str) -> None:
        self.devices = [d for d in self.devices if d.id != device_id]
        self.sensor_data.pop(device_id, None)

    # -> "Device | None": same `X | None` as references 4.5, with a custom
    # class as X. Quotes keep it a forward reference for consistency.
    def get_device(self, device_id: str) -> "Device | None":
        for device in self.devices:
            if device.id == device_id:
                return device
        return None

    def list_devices(self) -> list[Device]:
        return self.devices

    def update_sensor_data(self, sensor_id: str, timestamp: float, value: float) -> None:
        if sensor_id in self.sensor_data:
            self.sensor_data[sensor_id]["last_measurement_timestamp"] = timestamp
            self.sensor_data[sensor_id]["last_measurement_value"] = value

    def update_actuator_data(self, actuator_id: str, timestamp: float, status: str) -> None:
        if actuator_id in self.sensor_data:
            self.sensor_data[actuator_id]["last_status_change_timestamp"] = timestamp
            self.sensor_data[actuator_id]["status"] = status
