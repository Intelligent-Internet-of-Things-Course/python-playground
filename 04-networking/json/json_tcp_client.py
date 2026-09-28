"""
Networking hands-on (JSON) - TCP client that sends a ServiceMessage as JSON.

Run:  python3 json_tcp_client.py --host 127.0.0.1 --port 65432
"""

import argparse
import logging
import socket

from iot_device import IoTDevice
from service_message import ServiceMessage

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("json_tcp_client")

BUFFER_SIZE = 1024


def main() -> None:
    parser = argparse.ArgumentParser(description="JSON-over-TCP client.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=65432)
    args = parser.parse_args()

    device = IoTDevice("device-0001", "acme-inc", "v0.0.1-beta", 44.101010, 10.421321)
    logger.info("device: %s", device)

    message = ServiceMessage("CREATE-DEVICE", device)
    payload = message.to_json()
    logger.info("sending: %s", payload)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args.host, args.port))
        s.sendall(payload.encode())
        data = s.recv(BUFFER_SIZE)

    logger.info("server replied: %s", data.decode(errors="replace"))


if __name__ == "__main__":
    main()
