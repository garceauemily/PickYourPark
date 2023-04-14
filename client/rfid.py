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

def GetCUID():
	if not TestMode:
		global ReturnIDs
		ReturnIDs = []
		start_time = time.time()
		while True:
			current_time = time.time()
			elapsed_time = current_time - start_time
			if elapsed_time > 2:
				break
			FoundTags = reader.read()
			for Tag in FoundTags:
				if Tag.user_mem_data not in ReturnIDs:
					ReturnIDs.append(Tag.user_mem_data)
		if ReturnIDs == []:
			ReturnIDs.append(b"00000000")
		return ReturnIDs
	else:
		return b"00000000"