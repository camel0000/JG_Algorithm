# 23-04-30
# 2502 : 떡 먹는 호랑이

import sys
input = sys.stdin.readline

D, K = map(int, input().split())

a = 1
b = 1

ddeok = [0 for _ in range(D + 1)]

ddeok[1] = a
ddeok[2] = b

while 1:
    for i in range(3, D + 1):
        ddeok[i] = ddeok[i - 2] + ddeok[i - 1]
    
    if ddeok[D] == K:
        break
    elif ddeok[-1] > K:
        ddeok[1] += 1
        ddeok[2] = ddeok[1]
    else :
        ddeok[2] += 1
print(ddeok[1])
print(ddeok[2])