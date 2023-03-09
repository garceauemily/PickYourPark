#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import threading as th
import sys

push = 18
fsr1 = 31
fsr2 = 37

press = 0

run = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(push, GPIO.IN)
GPIO.setup(fsr1, GPIO.IN)
GPIO.setup(fsr2, GPIO.IN)

lock1 = 1
lock2 = 1

def FSR1():
        global lock1
        global press
        lock1 = 0
        print("FSR1 Tripped (Counting up)")
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
        while GPIO.input(fsr2):
                temp = 1
        press = press - 1
        print("Count: ", press)
        lock2 = 1

def STOP():
        run = 0

while run:
        if GPIO.input(fsr1) and lock1:
                F1 = th.Thread(target=FSR1)
                F1.start()
        if GPIO.input(fsr2) and lock2:
                F2 = th.Thread(target=FSR2)
                F2.start()

GPIO.cleanup()
