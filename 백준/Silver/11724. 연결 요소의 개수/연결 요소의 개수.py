# DFS & BFS (깊이우선탐색 & 너비우선탐색)
# 11724번 연결 요소의 개수

import sys
sys.setrecursionlimit(3000)

def dfs(v):
    visited[v] = 1
    
    for i in G[v]:
        if not visited[i]:
            dfs(i)

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    G[x].append(y)
    G[y].append(x)

visited = [0] * (N + 1)
count_ = 0

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count_ += 1

print(count_)