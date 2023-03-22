# 21606 : 아침 산책

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip()))

graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(0)