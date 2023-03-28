# echo-server.py

import socket
import struct
from connection import *


IoO = 2
CUID = '11111111'

HOST = "169.254.185.103"  # This is the IP of the admin PC. This needs to be set statically
PORT = 5005  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket created at %s:%d" % (HOST, PORT))
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(9)
            if data:
                print(struct.unpack('?8s',data))
                IoO = data[0]
                CUID = data[1]
                updateDatabase(IoO, CUID)

#conn.sendall(data)
