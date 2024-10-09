import socket
from iot_device import IoTDevice
from service_message import ServiceMessage

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

iotDevice = IoTDevice("device-0001", "acme-inc", "v0.0.1-beta", 44.101010, 10.421321)
print(iotDevice)

serviceMessage = ServiceMessage("CREATE-DEVICE", iotDevice)
msgFromClient = serviceMessage.to_json()
print(msgFromClient)

bytesToSend = str.encode(msgFromClient)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytesToSend)
    data = s.recv(1024)
    s.close()

print('Received', repr(data))