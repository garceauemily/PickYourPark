#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import threading as th

push = 18	# pin number for push button
fsr1 = 31	# pin number for the enter FSR
fsr2 = 37	# pin number for the exit FSR

press = 0 	# for total car count
run = 1		# for the push button to stop the program

# setting up the pins for the push button / FSRs
GPIO.setmode(GPIO.BOARD)
GPIO.setup(push, GPIO.IN)
GPIO.setup(fsr1, GPIO.IN)
GPIO.setup(fsr2, GPIO.IN)

# defining locks so multiple threads aren't made for one car
lock1 = 1
lock2 = 1

def FSR1():
	# defining globals so they can be changed within the method
	global lock1
	global press

	lock1 = 0 # one thread takes the key and prevents other threads from running the same method
	print("FSR1 Tripped (Counting up)")

	# waits for the enter FSR to not be pressed
	while GPIO.input(fsr1):
		temp = 1

	# outputs the new car total
	press = press + 1
	print("Count: ", press)

	lock1 = 1 # allows another thread to run the method

def FSR2():
	# defining globals so that can be changed within the method
	global lock2
	global press

	lock2 = 0 # one thread takes the key and prevents other threads from running the same method
	print("FSR2 Tripped (Counting down)")

	# waits for the exit FSR to not be pressed
	while GPIO.input(fsr2):
		temp = 1

	# outputs the new car total
	press = press - 1
	print("Count: ", press)

	lock2 = 1 # allows another thread to run the method

# stops the program
def STOP():
	run = 0

while run:
	# if the enter FSR is pressed and the method isn't being run
	if GPIO.input(fsr1) and lock1:
		# create a thread and run FSR1()
		F1 = th.Thread(target=FSR1)
		F1.start()
	# if the exit FSR is pressed and the method isn't being run
	if GPIO.input(fsr2) and lock2:
		# create a thread and run FSR2()
		F2 = th.Thread(target=FSR2)
		F2.start()

GPIO.cleanup()
