#!/usr/bin/env python3

import socket
import struct
import rfid
import RPi.GPIO as GPIO
import threading as th

HOST = "192.168.187.123"  # The server's hostname or IP address
PORT = 5005  # The port used by the server

IoO = 1
CUID = 12345678

#Interrupt routine
push = 18
fsr1 = 31
fsr2 = 37
led  = 16
press = 0
run = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(push, GPIO.IN)
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
        doSend(1)
        while GPIO.input(fsr1):
            temp = 1
        press = press + 1
        print("Count: ", press)
        lock1 = 1

def FSR2():
        global lock2
        global press
        lock2 = 0
        print("FSR2 Tripped (Counting down)")
        doSend(0)
        while GPIO.input(fsr2):
            temp = 1
        press = press - 1
        print("Count: ", press)
        lock2 = 1

def STOP():
        run = 0

def doSend(IoO):
        CUID = rfid.GetCUID()
        packet = struct.pack('?8s', IoO, CUID)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(packet)
                s.settimeout(5)
                data = s.recv(4)
                if data == b"full":
                        toggleLED(1)
                else:
                        toggleLED(0)
                s.close()

def toggleLED(full):
      if full == 1:
        GPIO.output(led, GPIO.HIGH)
      else:
        GPIO.output(led, GPIO.LOW)

while True:
        # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #         s.connect((HOST, PORT))
        #         while True:
        if GPIO.input(fsr1) and lock1:
                F1 = th.Thread(target=FSR1)
                F1.start()
        if GPIO.input(fsr2) and lock2:
                F2 = th.Thread(target=FSR2)
                F2.start()
