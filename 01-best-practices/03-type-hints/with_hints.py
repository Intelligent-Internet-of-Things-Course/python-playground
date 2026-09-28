"""
Best practices hands-on - Step 03b: type hints + isinstance() together.

Run:  python3 with_hints.py

Key point: the hints (list[float], float, float | None, str) are DOCUMENTATION
only - they do not stop the wrong value. The isinstance() checks are what
actually enforce anything. Try:  mypy with_hints.py  to see the hints checked.
"""

def add_reading(readings: list[float], value: float) -> None:
    # the hint would NOT stop a string; this check does - and it excludes
    # bool on purpose (bool is a subclass of int, section 4.3)
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"reading must be a number, got {type(value).__name__}")
    readings.append(float(value))

def average_reading(readings: list[float]) -> float | None:
    # the "| None" is made TRUE by this check, not just claimed by the hint
    if not readings:
        return None
    return sum(readings) / len(readings)

def main() -> None:
    sensor_1: list[float] = []
    add_reading(sensor_1, 21.5)
    add_reading(sensor_1, 22.0)
    print("average:", average_reading(sensor_1))

    try:
        add_reading(sensor_1, "not-a-number")     # blocked by isinstance(), not the hint
    except TypeError as e:
        print("rejected:", e)

    try:
        add_reading(sensor_1, True)               # bool rejected explicitly
    except TypeError as e:
        print("rejected:", e)

    print("average of empty sensor:", average_reading([]))   # None, not a crash

    # the str hint here is never checked anywhere -> this silently "works"
    device_id: str = 12345
    print("device_id:", device_id, "->", type(device_id).__name__)

if __name__ == "__main__":
    main()
