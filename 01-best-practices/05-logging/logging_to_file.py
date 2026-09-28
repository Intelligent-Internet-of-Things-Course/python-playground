"""
Best practices hands-on - Step 05b: sending logs to a file.

Run:  python3 logging_to_file.py
Then: cat smart_home.log     (the *.log file is git-ignored)

Note the %(asctime)s field: timestamps for free, something a bare print()
never gives you.
"""

import logging
from pathlib import Path

LOG_FILE = Path(__file__).parent / "smart_home.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    filename=LOG_FILE,
)
logger = logging.getLogger("smart_home")

def main():
    logger.info("Device sensor_1 started")
    logger.warning("Battery level low: 15%")
    logger.error("Failed to reach the device")
    print(f"3 records written to {LOG_FILE.name} (nothing printed to the terminal by logging)")

if __name__ == "__main__":
    main()
