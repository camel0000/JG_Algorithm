# 2798 : 블랙잭

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_list = list(map(int, input().split()))

R = 0
    
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if _list[i] + _list[j] + _list[k] > M:
                continue
            else:
                R = max(R, _list[i] + _list[j] + _list[k])
print(R)