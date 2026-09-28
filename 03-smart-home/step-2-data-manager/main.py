"""
Run:  python3 main.py

Walk-through (python_oop.md 5):
  1. the DataManager stores devices and a snapshot of their latest data;
  2. add / get / list / remove all go through it;
  3. updating a sensor reading is reflected in sensor_data.
"""

from sensors import TemperatureSensor, HumiditySensor
from actuators import SmartLight
from data_manager import DataManager


def main() -> None:
    dm = DataManager()

    t = TemperatureSensor("sensor_1", 22.5)
    h = HumiditySensor("sensor_2", 45.0)
    light = SmartLight("bulb_1")

    for d in (t, h, light):
        dm.add_device(d)

    print("devices:", [d.id for d in dm.list_devices()])
    print("get_device('sensor_2') ->", dm.get_device("sensor_2").type)

    # a new reading, pushed through the manager
    t.update_value()
    dm.update_sensor_data("sensor_1", t.last_measurement_timestamp, t.last_measurement_value)
    print("sensor_1 snapshot ->", dm.sensor_data["sensor_1"])

    dm.remove_device("bulb_1")
    print("after remove ->", [d.id for d in dm.list_devices()])


if __name__ == "__main__":
    main()
