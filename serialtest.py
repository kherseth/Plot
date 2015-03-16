# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:01:09 2015

@author: kim
"""

import serial

ser = serial.Serial();

ser.setBaudrate(38400)
ser.setPort("COM4")
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
#    ser.XonXoff = False
#    ser.rtscts = False
#    ser.dsrdtr = False
ser.timeout = 500
ser.open()
ser.isOpen()
print('Port Opened')
print(ser.isOpen())
while ser.isOpen():
    print(ser.readline())