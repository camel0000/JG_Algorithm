# 14728_02 : 벼락치기

import sys
input = sys.stdin.readline

N, T = map(int, input().split())

dp = [[0] * (T + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    ex_T, point = map(int, input().split())
    
    for j in range(1, T + 1):
        if j - ex_T >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - ex_T] + point)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])