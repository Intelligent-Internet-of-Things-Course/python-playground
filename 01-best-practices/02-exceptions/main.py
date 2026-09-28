"""
Best practices hands-on - Step 02: exception handling.

Run:  python3 main.py

Walk-through:
  1. a single specific except;
  2. several except clauses + `except Exception as e`;
  3. else (no error) / finally (always);
  4. a custom ConfigError carrying the missing key.
"""

class ConfigError(Exception):
    """Raised when a required configuration value is missing."""

    def __init__(self, key, message="Missing required configuration value"):
        self.key = key
        self.message = message
        super().__init__(f"{message}: '{key}'")

def load_setting(config, key):
    if key not in config:
        raise ConfigError(key)
    return config[key]

def main():
    # 3.1 - one specific exception
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: division by zero is not allowed.")

    # 3.1 - multiple clauses
    try:
        value = int("abc")
        print(10 / value)
    except ValueError:
        print("Error: could not convert string to integer.")
    except ZeroDivisionError:
        print("Error: division by zero.")
    except Exception as e:
        print(f"Other error: {e}")

    # 3.2 - else + finally
    try:
        value = int("42")
        print("Conversion successful.")
    except ValueError:
        print("Conversion failed.")
    else:
        print("No errors occurred.")
    finally:
        print("This always executes.")

    # 3.3 - custom exception
    try:
        load_setting({"device_id": "sensor_1"}, "sample_rate_seconds")
    except ConfigError as e:
        print(f"Custom exception caught: {e}  (key={e.key!r})")

if __name__ == "__main__":
    main()
