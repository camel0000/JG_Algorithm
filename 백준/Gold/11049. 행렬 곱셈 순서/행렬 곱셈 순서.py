# 11049 : 행렬 곱셈 순서

import sys
input = sys.stdin.readline

N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(1, N):
    for j in range(N - i):
        x = j + i
        dp[j][x] = 2 ** 32
        
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + info[j][0] * info[k][1] * info[x][1])
print(dp[0][N - 1])