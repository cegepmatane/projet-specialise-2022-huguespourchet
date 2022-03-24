# """
# A simple Python script to send messages to a sever over Bluetooth
# using PyBluez (with Python 2).
# """
#
# import bluetooth
#
# serverMACAddress = 'DC:F5:05:BA:EF:CA'
# port = 3
# s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# s.connect((serverMACAddress, port))
# while 1:
#     text = input() # Note change to the old (Python 2) raw_input
#     if text == "quit":
#         break
#     s.send(text)
# s.close()

"""
A simple Python script to send messages to a sever over Bluetooth using
Python sockets (with Python 3.3 or above).
"""

import socket

serverMACAddress = 'DC:F5:05:BA:EF:CA'
port = 8880
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(bytes(text, 'UTF-8'))
s.close()
