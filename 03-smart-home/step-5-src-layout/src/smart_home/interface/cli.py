"""Command-line entry point.

Ties together every best practice from the lecture:
  - if __name__ == "__main__" + a minimal main()      (2.x)
  - argparse for CLI options                           (5.2)
  - a YAML config file                                 (5.4)
  - logging instead of print()                         (6)
  - absolute imports across the package                (10.3)

Run (from the step-5-src-layout/ directory):
  python3 run.py
  python3 run.py --config config/settings.yaml --verbose
  PYTHONPATH=src python3 -m smart_home.interface.cli
"""

import argparse
import logging
import sys
from pathlib import Path

from smart_home.devices import TemperatureSensor, HumiditySensor, SmartLight, Sensor, Actuator
from smart_home.storage import DataManager
from smart_home.home import SmartHome
from smart_home.logic import apply_temperature_rule

logger = logging.getLogger("smart_home")

DEFAULT_CONFIG = Path(__file__).resolve().parents[3] / "config" / "settings.yaml"


def load_config(path: Path) -> dict:
    try:
        import yaml
    except ModuleNotFoundError:
        sys.exit("PyYAML not installed. Run:  pip install -r requirements.txt")
    with open(path) as f:
        return yaml.safe_load(f)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Smart Home IoT demo runner.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG,
                        help=f"path to settings.yaml (default: {DEFAULT_CONFIG})")
    parser.add_argument("--verbose", action="store_true", help="show DEBUG logs")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    config = load_config(args.config)
    logger.info("loaded config from %s", args.config)

    data_manager = DataManager()
    home = SmartHome(config["home_id"], config["latitude"], config["longitude"], data_manager)

    temperature = TemperatureSensor("sensor_1")
    humidity = HumiditySensor("sensor_2")
    light = SmartLight("bulb_1")
    for device in (temperature, humidity, light):
        home.add_device(device)

    temperature.update_value()
    humidity.update_value()
    logger.debug("temperature reading: %.2f", temperature.last_measurement_value)

    # the logic/ layer reacts to the reading
    apply_temperature_rule(temperature, light, config["temperature_threshold"])

    for device in home.list_devices():
        if isinstance(device, Sensor):
            logger.info("%s -> %.2f", device.id, device.last_measurement_value)
        elif isinstance(device, Actuator):
            logger.info("%s -> %s", device.id, device.status)


if __name__ == "__main__":
    main()
