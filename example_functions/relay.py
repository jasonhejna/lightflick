#!/usr/bin/env python

# Turn on a relay for N seconds

# TODO: The Thread need to shut itself down gracefully

import RPi.GPIO as GPIO, threading, time


def turn_on_for(set_time):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(set_time)
    GPIO.output(16, GPIO.LOW)
    GPIO.cleanup()


thread = threading.Thread(target=turn_on_for, args=(20))
thread.start()
thread.join()
print "thread finished...exiting"
