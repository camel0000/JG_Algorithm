# 1182 : 부분수열의 합

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(depth, _sum):
    global cnt
    
    if depth >= N:
        return
    
    _sum += seq[depth]
    
    if _sum == S:
        cnt += 1
        
    dfs(depth + 1, _sum)
    dfs(depth + 1, _sum - seq[depth])

N, S = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0

dfs(0, 0)

print(cnt)