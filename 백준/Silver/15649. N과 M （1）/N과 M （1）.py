# 15649 : N과 M (1)

import sys
input = sys.stdin.readline

def recursion(num):
    if num == M:
        print(' '.join(map(str, rs)))
        return
    
    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            rs.append(i)
            recursion(num + 1)
            visited[i] = 0
            rs.pop()

N, M = map(int, input().split())
rs = []
visited = [0] * (N + 1)

recursion(0)