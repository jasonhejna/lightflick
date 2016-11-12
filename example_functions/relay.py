#!/usr/bin/env python

# Turn on a relay for N seconds

# TODO: The Thread need to shut itself down gracefully

import RPi.GPIO as GPIO, threading, time


def turn_on_for():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(20)
    GPIO.output(16, GPIO.LOW)
    GPIO.cleanup()


def start():
    thread = threading.Thread(target=turn_on_for)
    thread.start()
    return thread.isAlive()


print start()
for i in range(0, 100):
    print i
    time.sleep(1)
