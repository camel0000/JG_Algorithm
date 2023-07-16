# 10974 : 모든 순열

import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
P = []
for i in range(1, N + 1):
    P.append(i)

for i in permutations(P):
    print(*i)