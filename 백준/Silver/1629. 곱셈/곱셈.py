# 1629 : 곱셈

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def DAC(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return DAC(a, b // 2, c) ** 2 % c
    else:
        return (DAC(a, b // 2, c) ** 2 * a) % c

print(DAC(a, b, c))