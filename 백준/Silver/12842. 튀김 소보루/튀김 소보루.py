# 23-05-03
# 12842 : 튀김 소보루

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
m = int(input())
times = [int(input()) for _ in range(m)]

total = 0
for i in range(1000000):
    for j in range(m):
        if i % times[j] == 0:
            total += 1
            if total == n - s:
                print(j + 1)
                exit()