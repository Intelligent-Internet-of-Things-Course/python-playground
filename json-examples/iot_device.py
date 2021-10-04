import json

class IoTDevice:

    def __init__(self, device_id, manufacturer, software_version, latitude, longitude):
        self.device_id = device_id
        self.manufacturer = manufacturer
        self.software_version = software_version
        self.latitude = latitude
        self.longitude = longitude

    # Replacement of the description method with the default __str__() method
    def __str__(self):
        return f"DeviceId: {self.device_id} - Manufacturer: {self.manufacturer} - Software Version: {self.software_version} - Lat/Lng: {self.latitude}/{self.longitude}"

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
