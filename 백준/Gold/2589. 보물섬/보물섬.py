# 2589 : 보물섬

import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    
    for i in range(M):
        for j in range(N):
            if maps[i][j] == 'L':
                q.append((i, j))
    
    while q:
        visited = [[0] * N for _ in range(M)]
        a, b = q.popleft()
        
        tmp_q = deque()
        tmp_q.append((a, b))
        visited[a][b] = 1
        
        while tmp_q:
            x, y = tmp_q.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and maps[nx][ny] == 'L':
                    visited[nx][ny] = visited[x][y] + 1
                    tmp_q.append((nx, ny))
        
        _max = 0
        for i in range(M):
            for j in range(N):
                _max = max(_max, visited[i][j])
        rs.append(_max)


M, N = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(M)]
rs = []

bfs()
print(max(rs) - 1)