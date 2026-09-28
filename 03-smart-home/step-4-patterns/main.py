"""
Run:  python3 main.py

Walk-through (python_oop.md 7.4 - 7.6), applied to the Smart Home:
  1. Singleton  - two DataManager() calls return the SAME object;
  2. Factory    - devices built from a type string; adding SmartLock touched
                  one class + one branch;
  3. Observer   - SmartHome notifies a dashboard and a logger; removing the
                  dashboard leaves only the logger notified.
"""

import singleton
import factory
import observer


def demo_singleton() -> None:
    print("--- Singleton (7.4) ---")
    dm1 = singleton.DataManager()
    dm2 = singleton.DataManager()
    print("dm1 is dm2 ->", dm1 is dm2)
    dm1.devices.append("sensor_1")
    print("dm2.devices ->", dm2.devices)     # sees dm1's change


def demo_factory() -> None:
    print("--- Factory (7.5) ---")
    made = [
        factory.DeviceFactory.create_device("temperature", "sensor_1"),
        factory.DeviceFactory.create_device("humidity", "sensor_2"),
        factory.DeviceFactory.create_device("lock", "lock_1"),
    ]
    print("types ->", [d.type for d in made])
    try:
        factory.DeviceFactory.create_device("unknown", "x")
    except ValueError as e:
        print("rejected:", e)


def demo_observer() -> None:
    print("--- Observer (7.6) ---")
    home = observer.SmartHome("home_1")
    dashboard = observer.DashboardObserver()
    logger = observer.LoggerObserver()
    home.add_observer(dashboard)
    home.add_observer(logger)
    home.set_state("ALARMED")            # both notified
    home.remove_observer(dashboard)
    home.set_state("SAFE")              # only the logger


def main() -> None:
    demo_singleton()
    demo_factory()
    demo_observer()


if __name__ == "__main__":
    main()
