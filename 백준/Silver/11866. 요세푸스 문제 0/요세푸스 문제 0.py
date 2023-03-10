# 11866 : 요세푸스 문제 0

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
dq = deque()

for i in range(1, N + 1):
    dq.append(i)

print('<', end='')
while len(dq) != 1:
    dq.rotate((K - 1) * -1)
    
    print(dq.popleft(), end=', ')
print(dq[0], end='')
print('>', end='')