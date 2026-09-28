"""DataManager (python_oop.md 5): owns device storage.

Swapping in-memory storage for a database would only mean changing THIS file.
"""

from smart_home.devices import Sensor, Actuator, Device


class DataManager:
    def __init__(self) -> None:
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

    def get_device(self, device_id: str) -> Device | None:
        for device in self.devices:
            if device.id == device_id:
                return device
        return None

    def list_devices(self) -> list[Device]:
        return self.devices
