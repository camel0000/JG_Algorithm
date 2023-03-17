# 2606 : 바이러스

import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    
def virus_computer(graph, v, visited):
    visited[v] = 1
    
    for i in sorted(graph[v]):
        if not visited[i]:
            virus_computer(graph, i, visited)


visited = [0] * (V + 1)
virus_computer(graph, 1, visited)
print(visited.count(1) - 1) # 1번 컴퓨터는 count 제외