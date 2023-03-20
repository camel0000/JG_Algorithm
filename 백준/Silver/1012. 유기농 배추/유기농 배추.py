# 1012 : 유기농 배추

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x, y):
    if 0 <= x < N and 0 <= y < M and sq[x][y] == 1:
        sq[x][y] = 0
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            dfs(nx, ny)
            
        return 1
    
    else:
        return 0

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    sq = [[0] * M for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        sq[x][y] = 1
    
    visited = [[0] * M for _ in range(N)]
    
    rs = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == 1:
                rs += 1
    print(rs)