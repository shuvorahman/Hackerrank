#!/bin/python

import sys


n,k,q = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
temp = a[:]
k = k%n
for i in range(n):
    temp[(i+k)%n] = a[i]
for a0 in xrange(q):
    m = int(raw_input().strip())
    print temp[m]

