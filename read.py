#!/usr/bin/env python

# Read the light level from a GPIO pin on a raspberry pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import time

class readLight:
    def instantiate(self, input_gpio):
        self.gpio = input_gpio
        self.gpio.setmode(self.gpio.BCM)
        self.RCPIN = 20

    def get_light_level(self):
        reading = 0
        self.gpio.setup(self.RCPIN, self.gpio.OUT)
        self.gpio.output(self.RCPIN, self.gpio.LOW)
        # 10 milliseconds
        time.sleep(0.01)

        self.gpio.setup(self.RCPIN, self.gpio.IN)
        # This takes about 1 millisecond per loop cycle
        while (self.gpio.input(self.RCPIN) == self.gpio.LOW):
            reading += 1
        return reading
