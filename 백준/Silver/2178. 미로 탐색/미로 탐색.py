# DFS & BFS (깊이우선탐색 & 너비우선탐색)
# 2178번 미로탐색

from collections import deque

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    
    dx = [-1, 1, 0, 0]      # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]      # 상, 하, 좌, 우
    
    while Q:
        x, y = Q.popleft()
        
        for i in range(4):  # 상하좌우 4가지 경우
            X = x + dx[i]   # 좌표 변경에 의한 새 X좌표
            Y = y + dy[i]   # 좌표 변경에 의한 새 Y좌표
            
            if X >= N or X < 0 or Y >= M or Y < 0 or (X == 0 and Y == 0):  # 좌표가 범위를 벗어나는 경우
                continue
            if matrix_[X][Y] == 0:  # 이동할 수 없는 칸은 무시
                continue
            if matrix_[X][Y] == 1:  # 이동 가능한 칸
                matrix_[X][Y] = matrix_[x][y] + 1   # 방문한 칸에 1을 누적하여 더함
                Q.append((X, Y))
    return matrix_[N-1][M-1]    # 방문 횟수의 누적 합인 마지막 칸의 값을 반환

N, M = map(int, input().split())

matrix_ = []
for _ in range(N):
    matrix_.append(list(map(int, input())))

# matrix_ = [0 for _ in range(N)]
# for i in range(N):
#     row_ = int(input())
#     matrix_[i] = list(map(int, str(row_)))

print(bfs(0, 0))