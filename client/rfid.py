#!/usr/bin/env python3
TestMode = 0
import time
ReturnIDs = []

try:
	import mercury
except ImportError:
	print("!-> Unable to import mercury library, RFID subsystem acting in test mode.")
	TestMode = 1

try:
	reader = mercury.Reader("tmr:///dev/ttyUSB0", baudrate=115200)
	reader.set_region("NA3")
	reader.set_read_plan([1], "GEN2", bank=["user"], read_power=2700)
except:
	if not TestMode:
		print("!->Unable to connect to RFID reader. Operating in test mode")
		TestMode = 1

def PrintModel():
	print(reader.get_model())
	print(reader.get_supported_regions())

def AddEPC(epc):
	global ReturnIDs
	if epc not in ReturnIDs and epc is not None:
		ReturnIDs.append(epc)
	#ReturnIDs.append(epc)

def GetCUID():
	if not TestMode:
		global ReturnIDs
		ReturnIDs = []
		reader.start_reading(lambda tag: AddEPC(tag.epc))
		time.sleep(3)
		reader.stop_reading()

		if ReturnIDs == []:
			ReturnIDs.append(b"000000000000000000000000")
		return ReturnIDs
	else:
		return b"000000000000000000000000"