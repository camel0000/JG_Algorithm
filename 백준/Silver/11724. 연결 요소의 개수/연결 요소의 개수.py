# 11724_02 : 연결 요소의 개수

# bfs 풀이

import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 1
    
    while q:
        X = q.popleft()
        
        for i in graph[X]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)
rs = 0

for i in range(1, N + 1):
    if visited[i] == 0:
        bfs(i)
        rs += 1
    
print(rs)