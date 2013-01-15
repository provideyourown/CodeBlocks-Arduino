#!/usr/bin/env python
import serial, sys
import time

serialPort = sys.argv[1]
ser = serial.Serial(
    port=serialPort,
    baudrate=1200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
ser.isOpen()

ser.close() # always close port
time.sleep(1) # delays for 1.0 seconds - anything less doesn't seem to work

print "Leonardo in bootloader mode"
