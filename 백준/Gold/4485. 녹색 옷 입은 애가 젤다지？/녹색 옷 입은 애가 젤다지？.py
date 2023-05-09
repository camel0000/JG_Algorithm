# 23-05-09
# 4485 : 녹색 옷 입은 애가 젤다지?

import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, (maps[0][0], 0, 0))
    dist[0][0] = 0
    
    while q:
        cost, x, y = heapq.heappop(q)
        
        if x == N - 1 and y == N - 1:
            print("Problem " + str(count) + ": " + str(cost))
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                ncost = cost + maps[nx][ny]
                
                if ncost < dist[nx][ny]:
                    dist[nx][ny] = ncost
                    heapq.heappush(q, (ncost, nx, ny))


count = 1

while 1:
    N = int(input())
    
    if N == 0:
        exit()
    
    maps = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF] * (N) for _ in range(N)]
    
    
    dijkstra()
    count += 1