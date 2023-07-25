# 1911 : 흙길 보수하기

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pools = []
for _ in range(N):
    pools.append(list(map(int, input().split())))
pools.sort(key=lambda x : x[0])

plank = pools[0][0]
total_count = 0

for start, end in pools:
    if plank > end:
        continue
    elif plank < start:
        plank = start
    
    dist = end - plank
    remainder = 1
    
    if dist % L == 0:
        remainder = 0
    count = dist // L + remainder
    plank += count * L
    
    total_count += count
print(total_count)