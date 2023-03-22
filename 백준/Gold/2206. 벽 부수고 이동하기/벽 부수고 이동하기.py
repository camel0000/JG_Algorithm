# 2206 : 벽 부수고 이동하기

import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, coin):
    q = deque()
    q.append((x, y, coin))
    
    visited[x][y][coin] = 1
    
    while q:
        x, y, coin = q.popleft()
        
        # 도착지에 도착한 경우
        if x == N - 1 and y == M - 1:
            return visited[x][y][coin]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if maps[nx][ny] == 0 and visited[nx][ny][coin] == 0:
                q.append((nx, ny, coin))
                visited[nx][ny][coin] = visited[x][y][coin] + 1
            
            if maps[nx][ny] == 1 and coin == 1:
                q.append((nx, ny, coin - 1))
                visited[nx][ny][coin - 1] = visited[x][y][coin] + 1
                
    return -1
    

N, M = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

print(bfs(0, 0, 1))