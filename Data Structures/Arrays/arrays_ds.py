#!/bin/python

# Problem 1: Arrays - DS:


import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print ' '.join(str(i) for i in arr)