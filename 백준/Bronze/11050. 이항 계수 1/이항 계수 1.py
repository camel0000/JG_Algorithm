# 11050 : 이항 계수 1

import sys
input = sys.stdin.readline

def factorial(x):
    if (x >= 1):
        return x * factorial(x - 1)
    else:
        return 1

N, K = map(int, input().split())

X = 0

if 0 <= K <= N:
    print(factorial(N) // (factorial(K) * factorial(N - K)))
elif K < 0:
    print(0)
else:
    print(0)