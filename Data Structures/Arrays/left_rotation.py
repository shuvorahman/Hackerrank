#!/bin/python
# Problem 4 : Left Rotation

inp = raw_input().strip().split(' ')
length = int(inp[0])
rotation = int(inp[1])
arr = raw_input().strip().split(' ')
copy = arr[:]
for i in range(length):
    arr[i] = copy[(i+rotation)%length]
print ' '.join(i for i in arr)