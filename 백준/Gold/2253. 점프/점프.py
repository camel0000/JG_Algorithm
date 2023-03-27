# 2253 : 점프

import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())

visited = [[] for _ in range(N + 1)]

smalls = set()
for _ in range(M):
    rock = int(input())
    smalls.add(rock)

def bfs():
    q = deque()
    q.append((1, 0, 0))
    
    while q:
        idx, jump, cnt = q.popleft()
        
        for x in [jump + 1, jump, jump - 1]:
            if x > 0:
                n_idx = idx + x
                
                if n_idx == N:
                    return cnt + 1
                
                if n_idx < N and n_idx not in smalls and x not in visited[n_idx]:
                    visited[n_idx].append(x)
                    q.append((n_idx, x, cnt + 1))
    return -1

print(bfs())