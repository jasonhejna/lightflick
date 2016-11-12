#!/usr/bin/env python

# Turn on a relay for N seconds

import RPi.GPIO as GPIO, time


def turn_on_for(set_time):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(set_time)
    GPIO.output(23, GPIO.LOW)
    GPIO.cleanup()

turn_on_for(30)
