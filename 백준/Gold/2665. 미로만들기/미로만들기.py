# 2655 : 미로만들기

import sys
input = sys.stdin.readline
from collections import deque

# 가중치 X -> BFS로 풀이가능

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1:
                    if board[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y]
                        queue.appendleft((nx, ny))
                    else:   # 검은 방인 경우
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))


N = int(input())
board = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[-1] * N for _ in range(N)]

bfs()
print(visited[N - 1][N - 1])