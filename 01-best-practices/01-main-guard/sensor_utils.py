"""
Best practices hands-on - Step 01: if __name__ == "__main__".

Run it two ways and compare:
  python3 sensor_utils.py     -> __name__ is "__main__", the guarded block runs
  python3 main_app.py         -> this file is imported, __name__ is "sensor_utils",
                                 the guarded block does NOT run
"""

def read_temperature():
    return 21.5

# top-level code: runs EVERY time the file is loaded (run OR imported)
print(f"sensor_utils loaded, __name__ is {__name__!r}")

def main():
    # 2.3 - keep the guarded block minimal: it only calls main()
    print("Running sensor_utils.py directly - starting the sensor loop...")
    print(read_temperature())

if __name__ == "__main__":
    main()
