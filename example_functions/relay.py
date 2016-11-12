#!/usr/bin/env python

# Turn on a relay for N seconds


# TODO: The Thread need to shut itself down gracefully

import RPi.GPIO as GPIO, threading, time


def turn_on_for(on_for_time):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(on_for_time)
    GPIO.output(16, GPIO.LOW)
    GPIO.cleanup()


def start(input_time):
    thread = threading.Thread(target=turn_on_for, args=[input_time]).start()
    return thread.isAlive()

start(20)
