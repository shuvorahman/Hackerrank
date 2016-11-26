#!/bin/python

import sys


n = float(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pos_count = 0
neg_count = 0
zero_count = 0
for i in arr:
    if i > 0:
        pos_count += 1
    elif i == 0:
        zero_count += 1
    else:
        neg_count += 1
print pos_count/n
print neg_count/n
print zero_count/n

