# 2178 : 미로 탐색

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input().rstrip())) for _ in range(N)]


def miro_bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M or (nx == 0 and ny == 0):  # 공간을 벗어나는 경우, 이동할 수 없는 칸인 경우
                continue
                
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))
    
    return miro[N - 1][M - 1]

print(miro_bfs(0, 0))