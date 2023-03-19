# 7569 : 토마토

import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())

# boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

boxes = []
queue = deque([])

for i in range(H):
    tmp = []
    
    for j in range(N):
        tmp.append(list(map(int, input().split())))
        
        for k in range(M):
            if tmp[j][k] == 1:
                queue.append([i, j, k])
    
    boxes.append(tmp)

# print(boxes[1][1][2]) # 2층에 있는, 2번째 row, 3번째 column의 토마토 => 1

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while queue:
    x, y, z = queue.popleft()
    
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and boxes[nx][ny][nz] == 0:
            queue.append([nx, ny, nz])
            boxes[nx][ny][nz] = boxes[x][y][z] + 1
            
day = 0

for i in boxes:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        day = max(day, max(j))
print(day - 1)