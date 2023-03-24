# 1904 : 01타일

import sys
input = sys.stdin.readline

N = int(input())

d = [0] * 1000001
d[1], d[2] = 1, 2

for i in range(3, N + 1):
    d[i] = (d[i - 1] + d[i - 2]) % 15746

print(d[N])