# 23-04-19
# 2644 : 촌수계산

import sys
input = sys.stdin.readline

def dfs(X):
    for i in graph[X]:
        if visited[i] == 0:
            visited[i] = visited[X] + 1
            dfs(i)


n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())    
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n + 1)

visited[a] = 1
dfs(a)

if visited[b] == 0:
    print(-1)
else:
    print(visited[b] - 1)