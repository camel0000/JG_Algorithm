# 1261 : 알고스팟

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == -1:
                    if maze[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y]
                        queue.appendleft((nx, ny))
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))


M, N = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[-1] * M for _ in range(N)]

bfs()
print(visited[N - 1][M - 1])