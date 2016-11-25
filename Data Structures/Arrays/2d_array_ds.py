#!/bin/python
# Problem 2 : 2D Array - DS 
import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
    
max = -1 * sys.maxint
for i in range(4):
    for j in range(4):
        val = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if val > max:
            max = val
print max