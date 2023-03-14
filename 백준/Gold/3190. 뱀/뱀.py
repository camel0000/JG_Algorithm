# 3190 : 뱀

import sys
input = sys.stdin.readline
from collections import deque

def change(d, c):
    # 상(0) 우(1) 하(2) 좌(3)
    # 오른쪽으로 회전 : 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
    # 왼쪽으로 회전 : 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1 방향
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d
    
# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def start():
    dt = 1          # 첫 방향 (오른쪽으로)
    time = 1        # 시간 변수 초기화
    y, x = 0, 0     # 첫 위치 초기화
    
    visited = deque([[y, x]])   # 방문한 위치
    board[y][x] = 2
    
    while 1:
        y, x = y + dy[dt], x + dx[dt]
        
        if 0 <= y < N and 0 <= x < N and board[y][x] != 2:
            if not board[y][x] == 1:        # 움직일 칸에 사과 X 경우
                tmp_y, tmp_x = visited.popleft()
                board[tmp_y][tmp_x] = 0     # 꼬리 제거
            
            board[y][x] = 2
            visited.append([y, x])
            
            if time in times.keys():
                dt = change(dt, times[time])
            time += 1
        else:   # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time


N = int(input())    # 보드 크기(한 변 길이)
K = int(input())    # 사과 개수

board = [([0] * N) for _ in range(N)]

for _ in range(K):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 1  # 사과 저장

L = int(input())    # 방향 전환 횟수
times = {}

for _ in range(L):
    X, C = input().split()      # X초 후, C 방향으로 전환
    times[int(X)] = C      # times dict에 key, value 저장

print(start())