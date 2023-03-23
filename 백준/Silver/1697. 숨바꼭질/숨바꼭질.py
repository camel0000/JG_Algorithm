# 1697 : 숨바꼭질

import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    
    while q:
        X = q.popleft()
        dX = [X - 1, X + 1, 2 * X]
        
        if X == K:
            return visited[X]
        
        for i in range(3):
            nX = dX[i]
            
            if 0 <= nX < 100001 and visited[nX] == 0:
                visited[nX] = visited[X] + 1
                q.append(nX)
                
    return visited[nX]
        

N, K = map(int, input().split())
visited = [0] * (100001)

print(bfs(N))