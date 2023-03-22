# 5427 : 불

import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    sec = 0
    breaker = 0
    
    sg_q = deque()
    f_q = deque()
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == '@':
                sg_q.append((i, j))
                visited[i][j] = 1
            if maps[i][j] == '*':
                f_q.append((i, j))
    
    while sg_q:        
        for _ in range(len(f_q)):
            x, y = f_q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == '.':
                    f_q.append((nx, ny))
                    maps[nx][ny] = '*'
        
        for _ in range(len(sg_q)):
            x, y = sg_q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 탈출 조건
                if nx >= h or nx < 0 or ny >= w or ny < 0:
                    breaker = 1
                    break
                
                if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == '.' and visited[nx][ny] == 0:
                    sg_q.append((nx, ny))
                    visited[nx][ny] = 1
                    maps[nx][ny] = '@'
                    maps[x][y] = '.'

        sec += 1
        if breaker == 1:
            break
    
    if breaker == 1:
        print(sec)
    else:
        print('IMPOSSIBLE')
                    

for _ in range(int(input())):
    w, h = map(int, input().split())
    maps = [list(input().rstrip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    
    bfs()