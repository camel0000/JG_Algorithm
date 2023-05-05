# 23-05-03
# 12842 : 튀김 소보루

import sys
import math
input = sys.stdin.readline

n, s = map(int, input().split())
m = int(input())
times = [int(input()) for _ in range(m)]

_lcm = 1
for t in times:
    _lcm = math.lcm(_lcm, t)
    
total_per_cycle = 0
for i in range(m):
    total_per_cycle += _lcm // times[i]

quot = (n - s) // total_per_cycle
n -= quot * total_per_cycle

if n == s:
    print(m)
    exit()

total = 0
for i in range(1000000):
    for j in range(m):
        if i % times[j] == 0:
            total += 1
            if total == n - s:
                print(j + 1)
                exit()