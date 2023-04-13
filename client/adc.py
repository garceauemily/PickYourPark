import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

class ADC:
	def __init__(self):
		# create the spi bus
		self._spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
		# create the cs (chip select)
		self._cs = digitalio.DigitalInOut(board.D5)
		# create the mcp object
		self._mcp = MCP.MCP3008(self._spi, self._cs)
		# create an analog input channel on pin 0
		self._chan0 = AnalogIn(self._mcp, MCP.P0)
		self._chan1 = AnalogIn(self._mcp, MCP.P1)

	def ReadChannel(self, channel = 0, debug = False):
		if channel == 1:
			ch = MCP.P1
		else:
			ch = MCP.P0

		chan = AnalogIn(self._mcp, ch)
		if debug:
			print('Raw ADC Value: ', chan.value)

		return chan.value
