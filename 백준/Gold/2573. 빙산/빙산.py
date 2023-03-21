# 2573 : 빙산

import sys
input = sys.stdin.readline
from collections import deque

def find_lump(visited, a, b):  # 덩어리 검사용    
    que = deque()
    que.append((a, b))
    visited[a][b] = 1
    
    while que:
        c, d = que.popleft()
        
        for i in range(4):
            nc = c + dx[i]
            nd = d + dy[i]
            
            if 0 <= nc < N and 0 <= nd < M and visited[nc][nd] == 0 and arr[nc][nd] != 0:
                visited[nc][nd] = 1
                que.append((nc, nd))

def melt_iceberg(): # 1년 과정 거친 빙산 부분들 녹여주기(값 빼주기)
    for i in range(N):
        for j in range(M):
            if tmp[i][j] > 0:
                arr[i][j] = arr[i][j] - tmp[i][j]
                
                if arr[i][j] < 0:
                    arr[i][j] = 0

def bfs():
    global year
    
    visited = [[0] * M for _ in range(N)]
    lumps = 0
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and visited[i][j] == 0:
                find_lump(visited, i, j)
                lumps += 1
    
    if lumps == 1: # 1년의 녹는 과정 계산
        q = deque()
        
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    q.append((i, j))
                    
        while q:
            x, y = q.popleft()
            
            for i in range(4):  # 각 빙산 부분의 4면 확인
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:    # 4면 중 범위 내에 있고, 바다이면, tmp에서 그 좌표에 count
                    tmp[x][y] += 1
        
        year += 1
        melt_iceberg()
    
    elif lumps >= 2:
        print(year)
        exit()
    else:
        print(0)
        exit()
    

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

year = 0

while 1:
    tmp = [[0] * M for _ in range(N)]
    bfs()