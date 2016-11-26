#!/bin/python

import sys


time = raw_input().strip().split(':')
if time[2][-2:] == 'AM':
    if time[0] == '12':
        time[0] = '00'
else:
    if time[0] != '12':
        time[0] = str(int(time[0]) + 12)
print time[0] + ':' + time[1] + ':' + time[2][:-2]

