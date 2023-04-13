#!/usr/bin/env python3
TestMode = 0

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

def GetCUID():
	if not TestMode:
		ReturnIDs = []
		FoundTags = reader.read()
		if FoundTags is not None:
			for Tag in FoundTags:
				print(Tag.user_mem_data)
				ReturnIDs.append(Tag.user_mem_data)
			return ReturnIDs
		else:
			return b'00000000'
	else:
		return b'00000000'