## `04-networking/` — sockets, with the best practices applied

Goal: minimal clients and servers, refactored to use `argparse`, `logging`,
and a clean shutdown.

| Folder | Contains |
|---|---|
| [`udp/`](udp/) | `udp_server.py` + `udp_client.py` — connectionless echo |
| [`tcp/`](tcp/) | `tcp_server.py` + `tcp_client.py` — connection-oriented echo |
| [`json/`](json/) | an `IoTDevice` / `ServiceMessage` model sent as JSON over TCP; shows nested-object serialization and rebuild |

Run a server, then its client, in two terminals, e.g.:

```bash
python3 udp/udp_server.py --port 20001
python3 udp/udp_client.py --port 20001 --message "hi"
```
