# 3055 : 탈출

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    S_q = deque()
    water_q = deque()
    
    # minutes = 0
    
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'S':
                visited[i][j] = 1
                S_q.append((i, j, 0))
            if board[i][j] == '*':
                water_q.append((i, j))
                
    while S_q:
        for _ in range(len(water_q)):
            x, y = water_q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == '.':
                    board[nx][ny] = '*'
                    water_q.append((nx, ny))
                    
        for _ in range(len(S_q)):
            x, y, time = S_q.popleft()
            
            if board[x][y] == 'D':
                return time
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 왔던 길을 다시 돌아가는 것 방지 위해, visited[nx][ny] == 0 조건 필요
                if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and board[nx][ny] != 'X' and board[nx][ny] != '*':
                    visited[nx][ny] = 1
                    S_q.append((nx, ny, time + 1))
                    # minutes += 1
    
    return 'KAKTUS'


r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * (c) for _ in range(r)]

print(bfs())