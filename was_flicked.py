#!/usr/bin/env python

# Monitor light level, and check for light flicks greater then 2,
# count flicks and return the number of flicks.

import sys
import math
import execute_functions


class DetermineSwitch:
    def __init__(self):
        self.i = 0
        self.average_light_level = 1500
        self.readings = []
        self.averages = []
        self.running_flick_counts = []
        self.callable_functions = {
            3: execute_functions.f3,
            4: execute_functions.f4,
            5: execute_functions.f5,
            6: execute_functions.f6,
            7: execute_functions.f7,
            8: execute_functions.f8
        }

    def store_reads(self, light_value):
        """Calculating the average of the last 4 light values, storing the resulting
           averages in self.averages list."""
        self.readings.append(light_value)
        self.i += 1
        if self.i % 4 == 0 and self.i != 0:
            running_light_level = 0
            for light_level in self.readings:
                running_light_level += int(light_level)
            self.average_light_level = running_light_level / 4
            self.averages.append(self.average_light_level)
            self.readings = []
            self.i = 0
            if len(self.averages) > 50:
                self.averages.pop(0)
                self.check_for_flick()

    def check_for_flick(self):
        """Check if the light was flicked more then 2 times. Count the number of times.
           Looking through self.averages to determine number of times there was a difference
           between the current value, and the next value in the list."""
        detected_flicks = 1
        for i in range(0, 48):
            #print self.averages[i], ' - ', self.averages[i + 1], ' = ', self.averages[i] - self.averages[i + 1]
            if abs(self.averages[i] - self.averages[i + 1]) > 1600:
                detected_flicks += 1
                i += 1
            elif abs(self.averages[i] - self.averages[i + 2]) > 1600:
                detected_flicks += 1
                i += 2
        self.running_flick_counts.append(math.floor(detected_flicks / 2))
        # wait an extra average iteration to determine if another flick is coming
        if len(self.running_flick_counts) > 4:  # num of items in list
            self.running_flick_counts.pop(0)
            if self.running_flick_counts[1] > 2:
                for j in range(0, 4):
                    if self.running_flick_counts[0] != self.running_flick_counts[j]:
                        return
                flick_count_output = self.running_flick_counts[0]
                self.averages = []
                self.running_flick_counts = []
                self.execute_function(flick_count_output)

    def read_light(self):
        """Infinite loop that will read the light level. There's a built in delay of 10ms in read.py."""
        import read
        while True:
            #time1 = time.time()
            self.store_reads(read.get_light_level())
            #print 'T:', time.time() - time1

    def unit_test(self):
        """Read unit test values from files in the unit_tests directory"""
        test_list = open('./unit_tests/unit_test_1').read().splitlines()
        for light_value in test_list:
            #time1 = time.time()
            self.store_reads(light_value)
            #print 'T:', time.time() - time1

    def execute_function(self, flick_count):
        self.callable_functions[int(flick_count)]()


# Run
DetermineSwitchClass = DetermineSwitch()
is_test = sys.argv[1] == 'test'
if is_test:
    print 'Unit Testing Starting...'
    DetermineSwitchClass.unit_test()
else:
    DetermineSwitchClass.read_light()
