# 14502 : 연구소

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    
    for i in range(N):
        for j in range(M):
            if copy_maps[i][j] == 2:
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1 and copy_maps[nx][ny] == 0:
                q.append((nx, ny))
                copy_maps[nx][ny] = 2
    
    count = 0
    for i in range(N):
        for j in range(M):
            if copy_maps[i][j] == 0:
                count += 1
    return count
    

N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

blanks = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            blanks.append((i, j))

max_list = []

for new_idx in combinations(blanks, 3):
    copy_maps = copy.deepcopy(maps)        # 항상 copy_maps는 초기화 (by deepcopy) -> 전체 순열 검사(bfs 이용)

    x0, y0 = new_idx[0]
    x1, y1 = new_idx[1]
    x2, y2 = new_idx[2]
    
    copy_maps[x0][y0] = 1
    copy_maps[x1][y1] = 1
    copy_maps[x2][y2] = 1
    
    max_list.append(bfs())
    
print(max(max_list))