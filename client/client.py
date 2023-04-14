#!/usr/bin/env python3

import socket
import struct
import rfid
import threading as th
from adc import ADC
import time

HOST = "192.168.187.123"  # The server's hostname or IP address
PORT = 5005  # The port used by the server

IoO = 1
CUID = 12345678
CarWeight = 32768 #65535/2
Lot = b"C02"

#Interrupt routine
fsr1 = 6
fsr2 = 26
led  = 23
press = 0
run = 1

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(fsr1, GPIO.IN)
GPIO.setup(fsr2, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

lock1 = 1
lock2 = 1

def FSR1():
    global lock1
    global press
    lock1 = 0
    print("FSR1 Tripped (Counting up)")
    while GPIO.input(fsr1):
        temp = 1
    print("Press 1")
    while not GPIO.input(fsr1):
        temp = 1
    while GPIO.input(fsr1):
        temp = 1
    print("Press 2")
    doSend(1)
    press = press + 1
    print("Count: ", press)
    lock1 = 1

def FSR2():
    global lock2
    global press
    lock2 = 0
    print("FSR2 Tripped (Counting down)")
    while GPIO.input(fsr2):
        temp = 1
    print("Press 1")
    while not GPIO.input(fsr2):
        temp = 1
    while GPIO.input(fsr2):
        temp = 1
    print("Press 2")
    doSend(0)
    press = press - 1
    print("Count: ", press)
    lock2 = 1

def STOP():
        run = 0

def doSend(IoO):
        CUID = rfid.GetCUID()
        print(CUID)
        if CUID == []:
            CUID = b"000000000000000000000000"
        for Tag in CUID:
            if Tag is not None:
                packet = struct.pack('?3s24s', IoO, Lot, Tag)
                ClientMultiSocket = socket.socket()
                try:
                        ClientMultiSocket.connect((HOST, PORT))
                        ClientMultiSocket.send(packet)
                        data = ClientMultiSocket.recv(4)
                        print(data)
                        if data == b"full":
                                toggleLED(1)
                        else:
                                toggleLED(0)
                except socket.error as e:
                        print(str(e))
                ClientMultiSocket.close()
                print("Client closed")

def toggleLED(full):
      if full == 1:
        print("LED on")
        GPIO.output(led, GPIO.HIGH)
      else:
        print("LED off")
        GPIO.output(led, GPIO.LOW)

#Setup ACD
adc = ADC()

print("Lot", Lot, "ready")
try:
    while True:
        if GPIO.input(fsr1) and lock1:
                F1 = th.Thread(target=FSR1)
                F1.start()
        if GPIO.input(fsr2) and lock2:
                F2 = th.Thread(target=FSR2)
                F2.start()
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
