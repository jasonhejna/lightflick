#!/usr/bin/env python

# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

# measured light level change = 2249
# percent allowance = 70%
# min light level change = 1574
# num of light switch flicks = 3

import read, sys


is_test = sys.argv[0] == 'test'
if is_test:
    import csv
    with open('file.csv', 'rb') as f:
        reader = csv.reader(f)
        test_list = list(reader)

count = 0
def read_test():
    count += 1
    return test_list[count]

i = 0
group = 0
averages = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
while True:
    if is_test:
        print read_test()
    else:
        single_reading = read.get_light_level()
        print single_reading

#TODO: throw away above and replace with reading into an array of arrays that's constantly shifting. Re-calc every 5 individual reads. 300 ms total.
