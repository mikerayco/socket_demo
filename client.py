import socket
import pickle

HEADER_SIZE = 10

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    full_msg = b""
    new_msg = True

    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADER_SIZE]}")
            print(f"partial message: {msg}")
            msglen = int(msg[:HEADER_SIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADER_SIZE == msglen:
            print("full message received")
            print(full_msg[HEADER_SIZE:])

            d = pickle.loads(full_msg[HEADER_SIZE:])
            print(d)
            new_msg = True
            full_msg = b""

