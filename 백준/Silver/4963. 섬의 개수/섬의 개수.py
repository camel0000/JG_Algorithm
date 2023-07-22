# 4963 : 섬의 개수

import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx <= h - 1 and 0 <= ny <= w - 1 and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
                
    

w, h = map(int, input().split())
while w != 0 and h != 0:
    maps = []
    for _ in range(h):
        maps.append(list(map(int, input().split())))
    
    visited = [[0 for _ in range(w)] for _ in range(h)]
    count = 0
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                count += 1
    print(count)
    w, h = map(int, input().split())