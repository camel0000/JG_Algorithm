# 23-05-16
# 6593 : 상범 빌딩

import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([sz, sy, sx])
    visited[sz][sy][sx] = 1
    
    while q:
        z, y, x = q.popleft()
        
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            
            if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C and visited[nz][ny][nx] == 0:
                if maps[nz][ny][nx] == "." or maps[nz][ny][nx] == "E":
                    dp[nz][ny][nx] = dp[z][y][x] + 1
                    visited[nz][ny][nx] = 1
                    q.append([nz, ny, nx])
            

while 1:
    L, R, C = map(int, input().split())     # 층, 행, 열
    if L == R == C == 0:
        break
    
    maps = [[] * R for i in range(L)]
    dp = [[[0] * C for i in range(R)] for i in range(L)]
    visited = [[[0] * C for i in range(R)] for i in range(L)]
    for i in range(L):
        for j in range(R):
            maps[i].append(list(map(str, input())))
        input()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if maps[i][j][k] == "S":
                    sx, sy, sz = k, j, i
                if maps[i][j][k] == "E":
                    ex, ey, ez = k, j, i
    
    bfs()
    if dp[ez][ey][ex] == 0:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)." % dp[ez][ey][ex])