"""
Networking hands-on - TCP echo server.

Best practices applied (python_best_practices.md):
  - argparse instead of hardcoded host/port   (5.2)
  - logging instead of print()                (6)
  - try/except + guaranteed socket close      (3.1 - 3.2)

Run:  python3 tcp_server.py --host 127.0.0.1 --port 65432
"""

import argparse
import logging
import socket

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("tcp_server")

BUFFER_SIZE = 1024


def main() -> None:
    parser = argparse.ArgumentParser(description="TCP echo server.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=65432)
    args = parser.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((args.host, args.port))
        server.listen()
        logger.info("waiting for incoming client connections on %s:%d", args.host, args.port)

        try:
            while True:
                conn, addr = server.accept()
                with conn:
                    logger.info("connected by %s", addr)
                    while True:
                        data = conn.recv(BUFFER_SIZE)
                        if not data:
                            logger.info("client %s disconnected", addr)
                            break
                        logger.info("received: %s", data.decode(errors="replace"))
                        conn.sendall(data)          # echo back
        except KeyboardInterrupt:
            logger.info("shutting down")


if __name__ == "__main__":
    main()
