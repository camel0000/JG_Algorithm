# 18352 : 특정 거리의 도시 찾기

import sys
input = sys.stdin.readline
from collections import deque

V, E, K, X = map(int, input().split())  # 도시 개수(V) / 도로 개수(M) / 거리 정보(K) / 출발 도시 번호(X)
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(S):
    queue = deque([S])
    visited[S] = 1
    
    while queue:
        v = queue.popleft()
        
        if visited[v] == K + 1:
            rs.append(v)
        
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1


visited = [0] * (V + 1)
rs = []

bfs(X)

if rs:
    rs.sort()
    
    for i in range(len(rs)):
        print(rs[i])
else:
    print(-1)