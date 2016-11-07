#!/usr/bin/env python

# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

# measured light level change = 2249
# percent allowance = 70%
# min light level change = 1574
# num of light switch flicks = 3

import sys
import time


#TODO: throw away above and replace with reading into an array of arrays that's constantly shifting. Re-calc every 5 individual reads. 300 ms total.


class DetermineSwitch:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.readings = []
        self.averages = []

    def store_reads(self, light_value):
        self.readings.append(light_value)
        self.i += 1
        if self.i % 5 == 0 and self.i != 0:
            running_light_level = 0
            for light_level in self.readings:
                running_light_level += int(light_level)
            average_light_level = running_light_level / 5
            self.averages.append(average_light_level)
            self.readings = []
            self.i = 0
            if len(self.averages) > 200:
                self.averages.pop(0)
                self.check_for_flick()

    def check_for_flick(self):
        print 'self.averages', self.averages
        #for average in self.averages:
        #    print average, '\n'

    def read_light(self):
        import read
        while True:
            self.store_reads(read.get_light_level())
            time.sleep(0.01)

    def unit_test(self):
        test_list = open('./unit_tests/unit_test_1').read().splitlines()
        for light_value in test_list:
            self.store_reads(light_value)


DetermineSwitchClass = DetermineSwitch()
is_test = sys.argv[1] == 'test'
if is_test:
    print 'Unit Testing'
    DetermineSwitchClass.unit_test()
else:
    DetermineSwitchClass.read_light()
