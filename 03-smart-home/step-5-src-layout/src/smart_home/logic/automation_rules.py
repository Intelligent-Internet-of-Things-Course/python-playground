"""Automation rules: built on top of devices/, independent of storage/ and interface/."""

import logging

from smart_home.devices import TemperatureSensor, SmartLight

logger = logging.getLogger(__name__)

def apply_temperature_rule(sensor: TemperatureSensor, light: SmartLight,
                           threshold: float) -> None:
    """If the temperature is above `threshold`, turn the light on; else off."""
    value = sensor.last_measurement_value
    if value is None:
        logger.warning("sensor %s has no reading yet; rule skipped", sensor.id)
        return

    if value > threshold:
        light.invoke_action("turn_on")
        logger.info("%.1f > %.1f -> light %s ON", value, threshold, light.id)
    else:
        light.invoke_action("turn_off")
        logger.info("%.1f <= %.1f -> light %s OFF", value, threshold, light.id)
