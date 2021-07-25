# -*- coding: utf-8 -*-
import numpy as np
import serial

# COM_PORT = 'COM3'  # set COM
# BAUD_RATES = 115200  # set baud rate
# ser = serial.Serial(COM_PORT, BAUD_RATES)  # initialize


def read_uart():
    COM_PORT = 'COM3'  # set COM
    BAUD_RATES = 115200  # set baud rate
    ser = serial.Serial(COM_PORT, BAUD_RATES)  # initialize
    while True:
        while ser.in_waiting:
            data_raw = ser.readline()
            data = data_raw.decode()
            a = data.rsplit("\r\r\n")
            b = a[0].split(",")
            b = np.array(b)
            c = [np.uint8(i) for i in b]
            return np.array(c)
            #return np.array([5, 10, 15, 20])

