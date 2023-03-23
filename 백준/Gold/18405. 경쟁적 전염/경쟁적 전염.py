# 18405_02 : 경쟁적 전염

import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    for a in range(N):
        for b in range(N):
            if maps[a][b] != 0:
                p, q, r = a, b, maps[a][b]
                c = 0
                tmp.append((p, q, r, c))

    tmp.sort(key=lambda x : x[2])
    
    q = deque(tmp)
    
    while q:
        x, y, vi, time = q.popleft()
        
        if time == S:
            break
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 0:
                maps[nx][ny] = vi
                q.append((nx, ny, vi, time + 1))
                

N, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

tmp = []

bfs()

print(maps[X - 1][Y - 1])