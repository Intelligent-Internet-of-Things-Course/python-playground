"""
Run:  python3 main.py

Walk-through (python_oop.md 3.1 - 3.3):
  1. a normal call succeeds;
  2. a low battery raises BatteryLowError, caught by type;
  3. the caught exception still carries .battery_level;
  4. else / finally show the full control flow.
"""

from battery import BatteryLowError, operate_electric_car


def main() -> None:
    for level in (55, 15):
        try:
            operate_electric_car(level)
        except BatteryLowError as error:
            print(f"Custom exception caught: {error}")
            print(f"  structured data -> battery_level = {error.battery_level}")
        else:
            print("  no exception: operation completed")
        finally:
            print("  (finally) check done for this level")


if __name__ == "__main__":
    main()
