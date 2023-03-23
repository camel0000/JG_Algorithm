# 2748 : 피보나치 수 2

import sys
input = sys.stdin.readline

N = int(input())

d = [0] * 91

def fibo(N):
    if N == 1 or N == 2:
        return 1
    
    if d[N] != 0:
        return d[N]
    
    d[N] = fibo(N - 1) + fibo(N - 2)
    return d[N]

print(fibo(N))