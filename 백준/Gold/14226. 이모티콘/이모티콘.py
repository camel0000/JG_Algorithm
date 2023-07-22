# 14266 : 이모티콘

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    
    # 이모티콘 = x, 클립보드 = y
    q.append((1, 0))
    visited[1][0] = 0
    
    while q:
        x, y = q.popleft()
        
        if visited[x][x] == -1:
            q.append((x, x))
            visited[x][x] = visited[x][y] + 1
        if x + y <= S and visited[x + y][y] == -1:
            q.append((x + y, y))
            visited[x + y][y] = visited[x][y] + 1
        if x - 1 >= 0 and visited[x - 1][y] == -1:
            q.append((x - 1, y))
            visited[x - 1][y] = visited[x][y] + 1
        

S = int(input())
visited = [[-1] * (S + 1) for _ in range(S + 1)]

bfs()
print(min([i for i in visited[S] if i != -1]))