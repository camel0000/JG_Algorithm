# 2667 : 단지번호붙이기

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):    
    q = deque()
    q.append((x, y))
    sq[x][y] = 0
    cnt = 1
    
    while q:
        a, b = q.popleft()
        
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            
            if 0 <= na < N and 0 <= nb < N and sq[na][nb] == 1:
                sq[na][nb] = 0
                q.append((na, nb))
                cnt += 1
    return cnt


N = int(input())
sq = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rs = []

for i in range(N):
    for j in range(N):
        if sq[i][j] == 1:
            rs.append(bfs(i, j))

rs.sort()

print(len(rs))
for i in range(len(rs)):
    print(rs[i])