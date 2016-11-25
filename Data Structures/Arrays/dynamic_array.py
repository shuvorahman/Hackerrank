#!/bin/python
#Problem 3 : Dynamic Array

data = raw_input().strip().split(' ')
no_of_seq = int(data[0])
no_of_q = int(data[1])

seqList = []
for i in range(no_of_seq):
    seqList.append([])
lastAns = 0
for i in range(no_of_q):
    query = raw_input().strip().split(' ')
    if query[0] == '1':
        seqList[(int(query[1]) ^ lastAns) % no_of_seq].append(int(query[2]))
    else:
        seq = seqList[(int(query[1]) ^ lastAns) % no_of_seq]
        try:
            lastAns = seq[int(query[2]) % len(seq)]
            print lastAns
        except IndexError:
            pass