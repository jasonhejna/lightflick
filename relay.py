#!/usr/bin/env python

# Turn on a relay for N seconds


# TODO: The Thread need to shut itself down gracefully

import threading, time


def run_for(GPIO, on_for_time):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(on_for_time)
    GPIO.output(16, GPIO.LOW)
    GPIO.cleanup()


def turn_on_relay_for(GPIO, input_time):
    thread = threading.Thread(target=run_for, args=[GPIO, input_time])
    thread.start()
