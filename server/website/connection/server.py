import socket
from _thread import *
import struct
from connection import *

def multi_threaded_client(conn):
	while True:
		data = conn.recv(12)
		if data:
				# full = 0
				print(struct.unpack('?8s',data))
				IoO = data[0]
				CUID = data[1]
				full = updateDatabase(IoO, "C02", CUID)
				if full:
					conn.send(b"full")
				else:
					conn.send(b"mpty")
		if not data:
			break
	conn.close()

ServerSideSocket = socket.socket()
host = "192.168.187.123"
port = 5005
ThreadCount = 0

try:
	ServerSideSocket.bind((host, port))
except socket.error as e:
	print(str(e))

ServerSideSocket.settimeout(3)
ServerSideSocket.listen(5)
print('Socket is listening..')

while True:
	try:
		Client, address = ServerSideSocket.accept()
		print('Connected to: ' + address[0] + ':' + str(address[1]))
		start_new_thread(multi_threaded_client, (Client, ))
		ThreadCount += 1
		print('Thread Number: ' + str(ThreadCount))
	except KeyboardInterrupt:
		print("Exiting")
		break
	except socket.timeout:
		pass
	finally:
		pass
exit()