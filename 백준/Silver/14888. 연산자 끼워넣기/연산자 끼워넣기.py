# 14888 : 연산자 끼워넣기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(depth, total, plus, minus, multi, div):
    global _max, _min
    
    if depth == N:
        _max = max(_max, total)
        _min = min(_min, total)
        
    if plus:
        dfs(depth + 1, total + A[depth], plus - 1, minus, multi, div)
    if minus:
        dfs(depth + 1, total - A[depth], plus, minus - 1, multi, div)
    if multi:
        dfs(depth + 1, total * A[depth], plus, minus, multi - 1, div)
    if div:
        dfs(depth + 1, int(total / A[depth]), plus, minus, multi, div - 1)


N = int(input())
A = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())

visited = [0] * (N + 1)

_max, _min = -1e9, 1e9

dfs(1, A[0], plus, minus, multi, div)
print(_max)
print(_min)