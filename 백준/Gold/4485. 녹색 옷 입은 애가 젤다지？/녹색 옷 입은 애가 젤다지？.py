# 23-04-03
# 4485 : 녹색 옷 입은 애가 젤다지?

import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0))
    dp[0][0] = arr[0][0]
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny]:
                    if dp[nx][ny] > dp[x][y] + arr[nx][ny]:
                        q.append((nx, ny))
                        dp[nx][ny] = min(dp[nx][ny], dp[x][y] + arr[nx][ny])
                else:
                    q.append((nx, ny))
                    dp[nx][ny] = dp[x][y] + arr[nx][ny]
                    visited[nx][ny] = 1


idx = 0
while 1:
    idx += 1
    N = int(input())
    if N == 0:
        break
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(N)]

    bfs()
    print("Problem " + str(idx) + ": " + str(dp[N - 1][N - 1]))