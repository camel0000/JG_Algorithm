# 11724_04 : 연결 요소의 개수
# dfs 풀이

import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

def dfs(v):
    visited[v] = 1
    
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (N + 1)
cnt = 0

for i in range(1, N + 1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)