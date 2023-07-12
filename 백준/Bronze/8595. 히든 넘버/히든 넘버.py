# 8595 : 히든 넘버

import sys
input = sys.stdin.readline

n = int(input())
word = input()

num = 0
_sum = 0
_flag = 0

for w in word:
    if _flag == 0:
        if w >= '0' and w <= '9':
            _flag = 1
            num += int(w)
            continue
        else:
            _sum += num
            num = 0
            
    if _flag == 1:
        if w >= '0' and w <= '9':
            _flag = 1
            num *= 10
            num += int(w)
            continue
        else:
            _sum += num
            num = 0
                        
print(_sum)