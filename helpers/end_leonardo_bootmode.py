#!/usr/bin/env python
import serial, sys
import time

time.sleep(1) # delays for 1.0 seconds - anything less doesn't seem to work

serialPort = sys.argv[1]
speed = sys.argv[2]

ser = serial.Serial(
    port=serialPort,
    baudrate=speed,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
ser.isOpen()

ser.close() # always close port

print "Leonardo is Ready"
