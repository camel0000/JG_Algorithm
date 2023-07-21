# 1303 : 전쟁 - 전투

import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

area = []
for i in range(M):
    area.append(list(input().strip()))
    
def W_bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    count = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx <= M - 1 and 0 <= ny <= N - 1 and visited[nx][ny] == 0 and area[nx][ny] == 'W':
                count += 1
                visited[nx][ny] = 1
                q.append([nx, ny])
    return count

def B_bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    count = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx <= M - 1 and 0 <= ny <= N - 1 and visited[nx][ny] == 0 and area[nx][ny] == 'B':
                count += 1
                visited[nx][ny] = 1
                q.append([nx, ny])
    return count

W_sum = 0
B_sum = 0
visited = [[0 for _ in range(N)] for _ in range(M)]

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and area[i][j] == 'W':
            W_sum += (W_bfs(i, j)**2)
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and area[i][j] == 'B':
            B_sum += (B_bfs(i, j)**2)
            
print(W_sum, B_sum)