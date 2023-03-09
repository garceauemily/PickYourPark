# Client Files

## This is the directory containing the client files which will run on the Raspberry Pi

### client.py

This program connects via socket to the server and will read RFID tag data
from the reader, pack the data, and send it to the server. It is based on
the following file - https://github.com/realpython/materials/blob/master/python-sockets-tutorial/echo-client.py

### rfid.py

This program is a module that provides various functions for interacting with
the Sparkfun m6e nano RFID reader
