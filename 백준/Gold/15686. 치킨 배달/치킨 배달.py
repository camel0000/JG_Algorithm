# 23-05-08
# 15686 : 치킨 배달

import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
        
rs = float('inf')

homes = []
chickens = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            homes.append((i, j))
        elif maps[i][j] == 2:
            chickens.append((i, j))

for c in combinations(chickens, M):
    total_distance = 0
    for r1, c1 in homes:
        dis = float('inf')
        for r2, c2 in c:
            dis = min(dis, abs(r1 - r2) + abs(c1 - c2))
        total_distance += dis
    rs = min(rs, total_distance)
print(rs)