#!/usr/bin/env python

# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)
RCPIN = 20


def get_light_level():
    reading = 0
    GPIO.setup(RCPIN, GPIO.OUT)
    GPIO.output(RCPIN, GPIO.LOW)
    # 10 milliseconds
    time.sleep(0.01)

    GPIO.setup(RCPIN, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCPIN) == GPIO.LOW):
        reading += 1
    return reading
