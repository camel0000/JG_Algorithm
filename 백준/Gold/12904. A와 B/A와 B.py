# 230405_12904 : A와 B

import sys
input = sys.stdin.readline
from collections import deque

S = deque(list(input().rstrip()))
T = deque(list(input().rstrip()))


while 1:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        tmp = deque()
        for t in reversed(T):
            tmp.append(t)
        T = tmp
    
    if S == T:
        print(1)
        exit()
    elif len(T) == 1 and S != T:
        print(0)
        exit()