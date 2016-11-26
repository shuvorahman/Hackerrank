#!/bin/python

import sys


size = int(raw_input().strip())
n = range(size)
a = []
for a_i in xrange(size):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    
corner_1 = sum([a[i][i] for i in n])
corner_2 = sum([a[i][size-i-1] for i in n])

print abs(corner_1 - corner_2)