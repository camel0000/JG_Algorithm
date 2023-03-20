# 11724_03 : 연결 요소의 개수

import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
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
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)    
cnt = 0

for i in range(1, N + 1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)