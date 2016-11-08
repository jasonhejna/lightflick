#!/usr/bin/env python

# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

# Re-calc light level every 5 individual reads. Loop through averages,
# comparing the current average to the next one. Calculate a diff greater
#  then 1700 to log a change in the lighting.

# measured light level change = 2249
# percent allowance = 70%
# min light level change = 1574
# num of light switch flicks = 3

import sys
import time
import math

class DetermineSwitch:
    def __init__(self):
        self.i = 0
        self.average_light_level = 1500
        self.readings = []
        self.averages = []
        self.number_of_flicks = 3

    def store_reads(self, light_value):
        self.readings.append(light_value)
        self.i += 1
        if self.i % 5 == 0 and self.i != 0:
            running_light_level = 0
            for light_level in self.readings:
                running_light_level += int(light_level)
            self.average_light_level = running_light_level / 5
            self.averages.append(self.average_light_level)
            self.readings = []
            self.i = 0
            if len(self.averages) > 200:
                self.averages.pop(0)
                self.check_for_flick()

    def check_for_flick(self):
        #print 'self.averages', self.averages
        detected_flicks = 1
        for i in range(0, 199):
            #print self.averages[i], ' - ', self.averages[i + 1], ' = ', self.averages[i] - self.averages[i + 1]
            diff1 = abs(self.averages[i] - self.averages[i + 1])
            if diff1 > 1700:
                detected_flicks += 1
                i += 1
        #if math.floor(detected_flicks / 2) > 2:
        print 'TOTAL FLICKS: ', math.floor(detected_flicks / 2)

    def read_light(self):
        import read
        while True:
            #time1 = time.time()
            self.store_reads(read.get_light_level())
            time.sleep(0.005)
            #print 'T:', time.time() - time1

    def unit_test(self):
        test_list = open('./unit_tests/unit_test_1').read().splitlines()
        for light_value in test_list:
            #time1 = time.time()
            self.store_reads(light_value)
            #print 'T:', time.time() - time1

DetermineSwitchClass = DetermineSwitch()
is_test = sys.argv[1] == 'test'
if is_test:
    print 'Unit Testing'
    DetermineSwitchClass.unit_test()
else:
    DetermineSwitchClass.read_light()