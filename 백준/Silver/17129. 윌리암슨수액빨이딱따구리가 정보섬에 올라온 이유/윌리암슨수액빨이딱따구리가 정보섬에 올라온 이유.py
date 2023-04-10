# 23-04-10
# 17129 : 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    q = deque()
    q.append((a, b, 0))
    visited[a][b] = 1
        
    while q:
        x, y, s = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            ns = s
            
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == '3' or arr[nx][ny] == '4' or arr[nx][ny] == '5':
                    return ns + 1
            
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != '1' and visited[nx][ny] == 0:
                q.append((nx, ny, ns + 1))
                visited[nx][ny] = 1
        
        # for i in range(N):
        #     for j in range(M):
        #         print(visited[i][j], end=' ')
        #     print()
        # print('---')
    return -1
        

for i in range(N):
    for j in range(M):
        if arr[i][j] == '2':
            second = bfs(i, j)
            break

if second == -1:
    print('NIE')
else:
    print('TAK')
    print(second)