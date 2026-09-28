"""
Networking hands-on (JSON) - TCP server that receives ServiceMessage JSON.

Best practices applied: argparse (5.2), logging (6), explicit JSON error
handling (3.1). Uses ServiceMessage.from_json() so the nested IoTDevice
comes back as a real object, not a dict.

Run:  python3 json_tcp_server.py --host 127.0.0.1 --port 65432
"""

import argparse
import logging
from json import JSONDecodeError
import socket

from service_message import ServiceMessage

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("json_tcp_server")

BUFFER_SIZE = 1024


def main() -> None:
    parser = argparse.ArgumentParser(description="JSON-over-TCP server.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=65432)
    args = parser.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((args.host, args.port))
        server.listen()
        logger.info("waiting for incoming client connections on %s:%d", args.host, args.port)

        conn, addr = server.accept()
        with conn:
            logger.info("connected by %s", addr)
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    conn.sendall(b"KO")
                    break
                received = data.decode("UTF-8")
                try:
                    logger.info("received message: %s", received)
                    message = ServiceMessage.from_json(received)
                    logger.info("parsed: %s", message)
                    logger.info("nested device is a %s", type(message.iot_device).__name__)
                    conn.sendall(b"OK")
                except (JSONDecodeError, KeyError) as e:
                    logger.error("error parsing received command: %s", e)
                    conn.sendall(b"KO")


if __name__ == "__main__":
    main()
