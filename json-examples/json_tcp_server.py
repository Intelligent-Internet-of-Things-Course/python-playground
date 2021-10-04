import socket
import json
from json import JSONDecodeError
from service_message import ServiceMessage

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting for incoming client connections ...")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            receivedString = data.decode('UTF-8')
            if len(data) > 0:
                try:
                    print("Received Message: {}".format(receivedString))
                    serviceMessage = ServiceMessage(**json.loads(receivedString))
                    print(serviceMessage)
                    conn.sendall(str.encode("OK"))
                except JSONDecodeError:
                    print("Error parsing received command !")
                    conn.sendall(str.encode("KO"))
            if not data:
                conn.sendall(str.encode("KO"))
                break
