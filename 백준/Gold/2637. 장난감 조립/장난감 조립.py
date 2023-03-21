# 2637_02 : 장난감 조립

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
needs = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    indegree[x] += 1

q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    X = q.popleft()
    
    for a, b in graph[X]:
        if needs[X].count(0) == N + 1:
            needs[a][X] += b   # a를 만들기 위해, X가 b만큼 필요
        else:
            for i in range(1, N + 1):
                needs[a][i] += needs[X][i] * b
                
        indegree[a] -= 1
        
        if indegree[a] == 0:
            q.append(a)

for i in range(1, N + 1):
    if needs[N][i] > 0:
        print(i, needs[N][i])