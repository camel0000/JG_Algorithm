# 23-05-19
# 2564 : 경비원

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
n = int(input())
dist = []

for _ in range(n + 1):
    x, y = map(int, input().split())
    
    # (0, 0) to 각 상점 distances
    if x == 1:  # 북
        dist.append(y)
    if x == 2:  # 남
        dist.append(r + c + r - y)
    if x == 3:  # 서
        dist.append(r + c + r + c - y)
    if x == 4:  # 동
        dist.append(r + y)

total = 0
for i in range(n):
    in_dist = abs(dist[-1] - dist[i])
    out_dist = 2 * (r + c) - in_dist
    total += min(in_dist, out_dist)
print(total)