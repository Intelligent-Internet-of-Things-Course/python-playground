"""
Networking hands-on - UDP client.

Run:  python3 udp_client.py --host 127.0.0.1 --port 20001 --message "Hello UDP Server"
"""

import argparse
import logging
import socket

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("udp_client")

BUFFER_SIZE = 1024


def main() -> None:
    parser = argparse.ArgumentParser(description="UDP client.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=20001)
    parser.add_argument("--message", default="Hello UDP Server")
    args = parser.parse_args()

    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    try:
        sock.sendto(args.message.encode(), (args.host, args.port))
        data, _ = sock.recvfrom(BUFFER_SIZE)
        logger.info("reply from server: %s", data.decode(errors="replace"))
    finally:
        sock.close()


if __name__ == "__main__":
    main()
