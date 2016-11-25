#!/bin/python
# Problem 5 : Sparse Arrays

no_of_str = int(raw_input().strip())
string_list = []
for i in range(no_of_str):
    string_list.append(raw_input().strip())
no_of_query = int(raw_input().strip())
for i in range(no_of_query):
    query = raw_input().strip()
    count = 0
    for j in string_list:
        if j == query:
            count += 1
    print count

