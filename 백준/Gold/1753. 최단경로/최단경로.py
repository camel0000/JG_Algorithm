import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
dist = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        d, n = heapq.heappop(q)
        
        if dist[n] < d:
            continue
        for x in graph[n]:
            cost = dist[n] + x[1]
            if cost < dist[x[0]]:
                dist[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))

dijkstra(k)

for i in range(1, v + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])