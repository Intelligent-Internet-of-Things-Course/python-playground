"""
Networking hands-on - UDP echo server.

Best practices applied (python_best_practices.md):
  - argparse instead of hardcoded host/port   (5.2)
  - logging instead of print()                (6)
  - graceful shutdown on Ctrl+C               (3.1)

Run:  python3 udp_server.py --host 127.0.0.1 --port 20001
"""

import argparse
import logging
import socket

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("udp_server")

REPLY = b"Hello UDP Client"
BUFFER_SIZE = 1024


def main() -> None:
    parser = argparse.ArgumentParser(description="UDP echo server.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=20001)
    args = parser.parse_args()

    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.bind((args.host, args.port))
    logger.info("UDP server up and listening on %s:%d", args.host, args.port)

    try:
        while True:
            message, address = sock.recvfrom(BUFFER_SIZE)
            logger.info("from %s: %s", address, message.decode(errors="replace"))
            sock.sendto(REPLY, address)
    except KeyboardInterrupt:
        logger.info("shutting down")
    finally:
        sock.close()


if __name__ == "__main__":
    main()
