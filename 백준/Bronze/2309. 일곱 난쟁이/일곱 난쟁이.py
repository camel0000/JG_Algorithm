# 2309 : 일곱 난쟁이

import sys
input = sys.stdin.readline

_list = []

for i in range(9):
    _list.append(int(input()))

_list.sort()

left = sum(_list) - 100


for i in range(9):
    for j in range(i + 1, 9):
        if _list[i] + _list[j] == left:
            idx_i = i
            idx_j = j            
            break

for i in range(9):
    if i != idx_i and i != idx_j:
        print(_list[i])