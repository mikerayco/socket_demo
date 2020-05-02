import socket
import time
import pickle


HEADER_SIZE = 10

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, addr = s.accept()
    print(f"Connection from {addr} has been established!")

    d = {1: "hey", 2: "there"}
    msg = pickle.dumps(d)

    msg = bytes(f"{len(msg):<{HEADER_SIZE}}", "utf-8") + msg

    clientsocket.send(msg)
    print(f"message sent: {msg}")
