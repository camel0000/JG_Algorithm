# 7562 : 나이트의 이동

import sys
input = sys.stdin.readline
from collections import deque

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    
    if i == ox and j == oy:
        return 0
        
    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx == ox and ny == oy:
                visited[nx][ny] = visited[x][y] + 1
                return
            
            if 0 <= nx <= l - 1 and 0 <= ny <= l - 1:
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


for _ in range(int(input())):
    l = int(input())
    x, y = map(int, input().split())
    ox, oy = map(int, input().split())
    
    visited = [[0 for _ in range(l)] for _ in range(l)]
    bfs(x, y)
    print(visited[ox][oy])