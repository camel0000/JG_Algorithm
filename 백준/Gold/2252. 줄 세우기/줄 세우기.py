# 2252 : 줄 세우기

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

indegree = [0] * (N + 1)
compared = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    compared[a].append(b)
    indegree[b] += 1


def makeRow():
    rs = []
    queue = deque()
    
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        now = queue.popleft()
        rs.append(now)
        
        for i in compared[now]:
            indegree[i] -= 1
            
            if indegree[i] == 0:
                queue.append(i)
                
    for i in rs:
        print(i, end=' ')

makeRow()