# 1260 : DFS와 BFS

import sys
input = sys.stdin.readline
from collections import deque

def DFS(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')
    
    for i in sorted(graph[v]):
        if not visited[i]:
            DFS(graph, i, visited)
            
def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
    
            
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    
visited = [0] * (N + 1)
DFS(graph, V, visited)
print()

visited = [0] * (N + 1)
BFS(graph, V, visited)