# 2231 : 분해 합

import sys
input = sys.stdin.readline

N = int(input())

M = 1

while M != 1000001:
    _M = M
    _sum = M
    
    while _M != 0:
        _sum += _M % 10
        _M //= 10
    
    if _sum == N:
        print(M)
        exit()
    else:
        M += 1
        
print('0')