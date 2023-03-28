# 2098 : 외판원 순회

import sys
input = sys.stdin.readline

def isIn(i, A):
    return (A & (1 << (i - 1))) != 0

def diff(A, j):
    t = 1 << (j - 1)
    return A & (~t)

def minimum(w, D, i, A):
    min_val = INF
    for j in range(1, n):
        if isIn(j, A):
            m = w[i][j] + D[j][diff(A, j)]
            min_val = min(min_val, m)
    return min_val

def travel(n, w):
    size = 2 ** (n - 1)
    D = [[0] * size for _ in range(n)]
    for i in range(1, n):
        D[i][0] = w[i][0]
    for k in range(1, n - 1):
        for A in range(1, size - 1):
            if bin(A).count('1') == k:
                for i in range(1, n):
                    if not isIn(i, A):
                        D[i][A] = minimum(w, D, i, A)
    A = size - 1
    return minimum(w, D, 0, A)

INF = int(1e9)
n = int(input())
w = []
for _ in range(n):
    w.append([INF if m == 0 else m for m in list(map(int, input().split()))])

print(travel(n, w))