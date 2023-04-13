import socket
from _thread import *
import struct
from connection import *

ServerSideSocket = socket.socket()
host = "169.254.185.103"
port = 5005
ThreadCount = 0

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

def multi_threaded_client(conn):
    conn.send(str.encode('Server is working:'))
    while True:
        data = conn.recv(0)
        if data:
                # full = 0
                print(struct.unpack('?8s',data))
                IoO = data[0]
                CUID = data[1]
                full = updateDatabase(IoO, CUID)
                if full:
                    conn.sendall(b"full")
                else:
                    print("here")
                    conn.sendall(b"mpty")
        if not data:
            break
    conn.close()

try:
	while True:
		Client, address = ServerSideSocket.accept()
		print('Connected to: ' + address[0] + ':' + str(address[1]))
		start_new_thread(multi_threaded_client, (Client, ))
		ThreadCount += 1
		print('Thread Number: ' + str(ThreadCount))
except KeyboardInterrupt:
	ServerSideSocket.close()