# Client Files

## This is the directory containing the client files which will run on the Raspberry Pi

### client.py

This program connects via socket to the server and will read RFID tag data
from the reader, pack the data, and send it to the server. It also contains code to interact with the FSRs and create threads for sensing input from the FSRs. It is based on
the client code model from - https://www.positronx.io/create-socket-server-with-multiple-clients-in-python/

### rfid.py

This program is a module that provides various functions for interacting with
the Sparkfun m6e nano RFID reader. It uses the Python Mercury API from Petr Gotthard - https://github.com/gotthardp/python-mercuryapi

### adc.py

This program is a module that provides functions for interacting with the MCP3008 10-bit ADC. It uses the Adafruit MCP3XXX module from - https://github.com/adafruit/Adafruit_CircuitPython_MCP3xxx

### fsr.py

This program contains code that was implemented directly into client.py. It is now deprecated, but here for visibility.
