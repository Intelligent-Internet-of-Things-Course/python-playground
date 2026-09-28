"""
Smart Home capstone - Step 3: the SmartHome class.

SmartHome represents the home (id + location) and exposes device-management
methods - but every one of them just DELEGATES to the DataManager. The
storage implementation can be swapped without changing this class.
"""

from device import Device
from data_manager import DataManager

class SmartHome:
    """Central entity of the Smart Home IoT system."""

    def __init__(self, home_id: str, latitude: float, longitude: float,
                 data_manager: DataManager) -> None:
        self.home_id = home_id
        self.latitude = latitude
        self.longitude = longitude
        self.data_manager = data_manager

    def add_device(self, device: Device) -> None:
        self.data_manager.add_device(device)

    def remove_device(self, device_id: str) -> None:
        self.data_manager.remove_device(device_id)

    def get_device(self, device_id: str) -> "Device | None":
        return self.data_manager.get_device(device_id)

    def list_devices(self) -> list[Device]:
        return self.data_manager.list_devices()
