import json

class ServiceMessage:
    def __init__(self, action_command, iot_device):
        self.action_command = action_command
        self.iot_device = iot_device

    # Replacement of the description method with the default __str__() method
    def __str__(self):
        return f"Action Command: {self.action_command} - Target IoT Device: {self.iot_device}"

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
