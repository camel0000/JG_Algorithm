# 2617 : 구슬 찾기

import sys
input = sys.stdin.readline
from collections import deque

def bfs_big(start):
    global cnt
    
    visited = []
    queue = deque([start])
    
    while queue:
        X = queue.popleft()
        
        if X not in visited:
            visited.append(X)
            queue.extend(graph_big[X])
            
    if len(visited) > mid_idx:
        cnt += 1
        
    return visited

def bfs_small(start):
    global cnt
    
    visited = []
    queue = deque([start])
    
    while queue:
        X = queue.popleft()
        
        if X not in visited:
            visited.append(X)
            queue.extend(graph_small[X])
            
    if len(visited) > mid_idx:
        cnt += 1
        
    return visited

    
N, M = map(int, input().split())

graph_big = [[] for _ in range(N + 1)]
graph_small = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph_big[b].append(a)
    graph_small[a].append(b)

cnt = 0
mid_idx = (N + 1) // 2

for i in range(1, N + 1):
    bfs_big(i)
    bfs_small(i)

print(cnt)