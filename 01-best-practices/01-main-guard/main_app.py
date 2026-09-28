"""
Run:  python3 main_app.py

This script only wants read_temperature(). Because sensor_utils.py guards its
"sensor loop" behind if __name__ == "__main__", importing it here does NOT
start that loop - only the top-level print() in sensor_utils runs.
(Compare with 2.2 in the lecture, where an unguarded file starts its loop on
import.)
"""

import sensor_utils


def main():
    print("main_app.py just needed the function, nothing else:")
    print(sensor_utils.read_temperature())


if __name__ == "__main__":
    main()
