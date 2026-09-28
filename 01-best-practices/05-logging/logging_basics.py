"""
Best practices hands-on - Step 05a: logging vs print().

Run:  python3 logging_basics.py

The DEBUG line does not appear: the configured threshold is INFO. Change
level=logging.INFO to level=logging.DEBUG and re-run - without touching any
logging call - to see it appear.
"""

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def main():
    logger.debug("This won't show, level is INFO")
    logger.info("Device sensor_1 started")
    logger.warning("Battery level low: 15%")
    logger.error("Failed to reach the device")
    logger.critical("Cannot connect to the gateway at startup")

if __name__ == "__main__":
    main()
