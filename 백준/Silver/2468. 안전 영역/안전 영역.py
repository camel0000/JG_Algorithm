# 2468 : 안전 영역

import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1 and area[nx][ny] != -1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])


N = int(input())
area = []
for _ in range(N):
    area.append(list(map(int, input().split())))

max_height = 1
for i in range(N):
    for j in range(N):
        max_height = max(area[i][j], max_height)

count_list = []

for h in range(0, max_height + 1):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    count = 0
    
    for i in range(N):
        for j in range(N):
            if area[i][j] == h:
                area[i][j] = -1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and 1 <= area[i][j] <= max_height:
                bfs(i, j)
                count += 1
    
    count_list.append(count)

print(max(count_list))