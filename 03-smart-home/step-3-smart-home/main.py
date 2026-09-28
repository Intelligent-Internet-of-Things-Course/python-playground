"""
Run:  python3 main.py

Full monitoring scenario (python_oop.md 6):
  1. build a DataManager and a SmartHome that delegates to it;
  2. add a temperature sensor, a humidity sensor and a smart light;
  3. take readings / switch the light on;
  4. iterate the devices and print sensor- vs actuator-specific data
     (isinstance() picks the right branch).
"""

import time

from sensors import Sensor, TemperatureSensor, HumiditySensor
from actuators import Actuator, SmartLight
from data_manager import DataManager
from smart_home import SmartHome


def main() -> None:
    data_manager = DataManager()
    smart_home = SmartHome("home_1", 37.7749, -122.4194, data_manager)

    temperature_sensor = TemperatureSensor("sensor_1", initial_temperature_value=22.5)
    humidity_sensor = HumiditySensor("sensor_2", initial_humidity_value=45.0)
    light_bulb = SmartLight("bulb_1", initial_status="OFF")

    for device in (temperature_sensor, humidity_sensor, light_bulb):
        smart_home.add_device(device)

    temperature_sensor.update_value()
    humidity_sensor.update_value()
    light_bulb.invoke_action("turn_on", None)

    time.sleep(1)

    for device in smart_home.list_devices():
        print(f"Device ID: {device.id}, Type: {device.type}, Manufacturer: {device.manufacturer}")
        if isinstance(device, Sensor):
            print(f"  Last measurement: {device.last_measurement_value:.2f} "
                  f"at {device.last_measurement_timestamp:.0f}")
        elif isinstance(device, Actuator):
            print(f"  Status: {device.status} at {device.last_status_change_timestamp:.0f}")


if __name__ == "__main__":
    main()
