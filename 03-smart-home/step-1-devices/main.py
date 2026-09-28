"""
Run:  python3 main.py

Walk-through (python_oop.md 4.4 - 4.8):
  1. the Device -> Sensor/Actuator -> concrete-class hierarchy;
  2. every concrete class implements the informal interface
     (update_value() / invoke_action());
  3. calling Sensor.update_value() directly raises NotImplementedError.
"""

from sensors import Sensor, TemperatureSensor, HumiditySensor
from actuators import SmartLight


def main() -> None:
    devices = [
        TemperatureSensor("sensor_1", initial_temperature_value=22.5),
        HumiditySensor("sensor_2", initial_humidity_value=45.0),
        SmartLight("bulb_1", initial_status="OFF"),
    ]

    # exercise each device through its own behaviour
    devices[0].update_value()
    devices[1].update_value()
    devices[2].invoke_action("turn_on")

    for d in devices:
        line = f"{d.id:<10} type={d.type:<18} mfr={d.manufacturer}"
        if isinstance(d, Sensor):
            line += f"  value={d.last_measurement_value:.2f} @ {d.last_measurement_timestamp:.0f}"
        else:
            line += f"  status={d.status} @ {d.last_status_change_timestamp:.0f}"
        print(line)

    # the base Sensor is an informal interface: this fails only when called
    try:
        Sensor("x", "Sensor", "Acme").update_value()
    except NotImplementedError as e:
        print("Sensor.update_value() ->", e)


if __name__ == "__main__":
    main()
