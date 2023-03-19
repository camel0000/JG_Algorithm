# 7576 : 토마토

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    v = [[0] * M for _ in range(N)]
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:      # 익은 토마토
                q.append((i, j))
                v[i][j] = 1
            elif box[i][j] == 0:    # 안익은 토마토
                cnt += 1
    
    while q:
        ci, cj = q.popleft()
        
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and box[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt -= 1
    
    if cnt == 0: return v[ci][cj] - 1
    else: return -1


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
ans = bfs()
print(ans)