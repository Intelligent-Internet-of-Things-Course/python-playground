"""
Networking hands-on - TCP client.

Run:  python3 tcp_client.py --host 127.0.0.1 --port 65432 --message "Hello, world"
"""

import argparse
import logging
import socket

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("tcp_client")

BUFFER_SIZE = 1024


def main() -> None:
    parser = argparse.ArgumentParser(description="TCP client.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=65432)
    parser.add_argument("--message", default="Hello, world")
    args = parser.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args.host, args.port))
        s.sendall(args.message.encode())
        data = s.recv(BUFFER_SIZE)

    logger.info("received: %s", data.decode(errors="replace"))


if __name__ == "__main__":
    main()
