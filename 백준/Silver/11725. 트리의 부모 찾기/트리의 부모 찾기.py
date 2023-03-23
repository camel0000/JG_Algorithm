# 11725_02 : 트리의 부모 찾기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)

dfs(1)
for i in range(2, N + 1):
    print(visited[i])